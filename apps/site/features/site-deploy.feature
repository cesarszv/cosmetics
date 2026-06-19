Feature: Site Deploy
  publish_pages.py publica el sitio estatico a GitHub Pages
  via git worktree con clean-tree guard y gh CLI.

  @s1
  Scenario: Working tree sucio aborta deploy
    Given cambios sin commitear en el working tree
    When publish_pages corre
    Then aborta con SystemExit antes de build
    And el mensaje menciona "working tree no esta limpio"

  @s2
  Scenario: Build falla aborta deploy
    Given un working tree limpio
    And build.py falla
    When publish_pages corre
    Then aborta con CalledProcessError antes de cualquier mutacion de git

  @s3
  Scenario: Primer deploy crea orphan branch
    Given un working tree limpio
    And build exitoso
    And sin branch gh-pages local ni remoto
    When publish_pages corre
    Then crea branch gh-pages como orphan
    And copia dist/ al root del worktree
    And commitea con mensaje "deploy: publish static site"
    And pushea a origin gh-pages

  @s4
  Scenario: Deploy con branch existente usa worktree
    Given un working tree limpio
    And build exitoso
    And branch gh-pages existe localmente
    When publish_pages corre
    Then usa git worktree add sobre gh-pages existente
    And copia dist/ al root
    And commitea y pushea si hay cambios

  @s5
  Scenario: No cambios para publicar
    Given un working tree limpio
    And build exitoso
    And dist/ identico al contenido actual de gh-pages
    When publish_pages corre
    Then imprime "No hay cambios para publicar en gh-pages."
    And no commitea ni pushea
    And configure_pages corre de todas formas

  @s6
  Scenario: Pages API falla sin abortar
    Given un deploy exitoso
    And gh api repos/{repo}/pages falla
    When configure_pages corre
    Then imprime instrucciones manuales
    And no raisea

  @s7
  Scenario: Pages se configura con gh-pages y root
    Given un deploy exitoso
    And Pages API responde
    When configure_pages corre
    Then setea source a branch gh-pages y path "/"

  @s8
  Scenario: Worktree se limpia al final
    Given un deploy completado o sin cambios
    When el contexto TemporaryDirectory termina
    Then git worktree remove --force corre
    And el worktree temporal se elimina

  @s9
  Scenario: .nojekyll se publica al root
    Given un build exitoso con .nojekyll en dist/
    When publish_pages copia dist/ al worktree
    Then .nojekyll existe en el root del worktree

  @s10
  Scenario: Clean directory antes de copiar dist
    Given un worktree gh-pages con archivos pre-existentes
    When copy_dist corre
    Then remueve todo excepto .git
    And copia el contenido de dist/ al root
