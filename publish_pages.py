from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
BRANCH = "gh-pages"


def run(command: list[str], cwd: Path = ROOT, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, check=check, text=True, capture_output=True)


def require_clean_worktree() -> None:
    status = run(["git", "status", "--porcelain"]).stdout.strip()
    if status:
        raise SystemExit(
            "El working tree no está limpio. Committeá o stasheá antes de publicar.\n"
            "Esto evita deployar una mezcla accidental de cambios."
        )


def repo_name_with_owner() -> str:
    result = run(["gh", "repo", "view", "--json", "nameWithOwner"])
    return json.loads(result.stdout)["nameWithOwner"]


def build_site() -> None:
    run([sys.executable, "build.py"])


def remote_branch_exists() -> bool:
    result = run(["git", "ls-remote", "--heads", "origin", BRANCH], check=False)
    return bool(result.stdout.strip())


def local_branch_exists() -> bool:
    result = run(["git", "show-ref", "--verify", f"refs/heads/{BRANCH}"], check=False)
    return result.returncode == 0


def prepare_pages_worktree(target: Path) -> None:
    if local_branch_exists():
        run(["git", "worktree", "add", str(target), BRANCH])
        return

    if remote_branch_exists():
        run(["git", "worktree", "add", "-b", BRANCH, str(target), f"origin/{BRANCH}"])
        return

    run(["git", "worktree", "add", "--detach", str(target), "HEAD"])
    run(["git", "checkout", "--orphan", BRANCH], cwd=target)
    clean_directory(target)


def clean_directory(path: Path) -> None:
    for item in path.iterdir():
        if item.name == ".git":
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


def copy_dist(target: Path) -> None:
    clean_directory(target)
    for item in DIST.iterdir():
        destination = target / item.name
        if item.is_dir():
            shutil.copytree(item, destination)
        else:
            shutil.copy2(item, destination)


def publish_worktree(target: Path) -> bool:
    run(["git", "add", "--all"], cwd=target)
    status = run(["git", "status", "--porcelain"], cwd=target).stdout.strip()
    if not status:
        print("No hay cambios para publicar en gh-pages.")
        return False

    run(["git", "commit", "-m", "deploy: publish static site"], cwd=target)
    run(["git", "push", "origin", BRANCH], cwd=target)
    return True


def configure_pages(repo: str) -> None:
    payload = json.dumps({"source": {"branch": BRANCH, "path": "/"}})
    get_result = run(["gh", "api", f"repos/{repo}/pages"], check=False)
    method = "PATCH" if get_result.returncode == 0 else "POST"
    process = subprocess.run(
        ["gh", "api", "--method", method, f"repos/{repo}/pages", "--input", "-"],
        cwd=ROOT,
        input=payload,
        text=True,
        capture_output=True,
    )
    if process.returncode != 0:
        print("No pude configurar GitHub Pages automáticamente.")
        print(process.stderr.strip())
        print("Configuralo manualmente: Settings → Pages → Deploy from a branch → gh-pages / root")
        return

    page = json.loads(process.stdout)
    print(f"GitHub Pages configurado: {page.get('html_url', 'revisá Settings → Pages')}")


def main() -> None:
    require_clean_worktree()
    repo = repo_name_with_owner()
    build_site()

    with tempfile.TemporaryDirectory(prefix="cosmetics-pages-") as tmp:
        target = Path(tmp) / "site"
        prepare_pages_worktree(target)
        copy_dist(target)
        published = publish_worktree(target)
        run(["git", "worktree", "remove", "--force", str(target)])

    configure_pages(repo)
    if published:
        print("Deploy enviado a gh-pages.")


if __name__ == "__main__":
    main()
