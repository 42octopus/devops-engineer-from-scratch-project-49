# Brain Games

[![Actions Status](https://github.com/42octopus/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/42octopus/devops-engineer-from-scratch-project-49/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=42octopus_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=42octopus_devops-engineer-from-scratch-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=42octopus_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=42octopus_devops-engineer-from-scratch-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=42octopus_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=42octopus_devops-engineer-from-scratch-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=42octopus_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=42octopus_devops-engineer-from-scratch-project-49)

**Brain Games** is a set of five fun console math games.  
They help you train your brain while having fun!

### Games
- **brain-even** — Is the number even?
- **brain-calc** — Solve math expressions (+, -, *)
- **brain-gcd** — Find the greatest common divisor
- **brain-progression** — Find the missing number in a progression
- **brain-prime** — Is the number prime?

### Installation

```bash
# 1. Build the package
make build

# 2. Install globally (recommended way)
make package-install
# or manually:
uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl
```

After installation all commands work directly (no `uv run` needed).

### How to play

Run any game and answer 3 questions correctly to win:

```bash
brain-games          # just greeting
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

You need to answer **yes/no** or enter the correct number.  
If you make a mistake, the game ends with the message "Let's try again, [name]!".

### Demo

**brain-even**  
[![asciicast](https://asciinema.org/a/dObBBIt4LLUHgWvA.svg)](https://asciinema.org/a/dObBBIt4LLUHgWvA)

**brain-gcd**  
[![asciicast](https://asciinema.org/a/Mj50A3YR9vPkwnSs.svg)](https://asciinema.org/a/Mj50A3YR9vPkwnSs)

**brain-progression**  
[![asciicast](https://asciinema.org/a/xnHSAucq78OOxHAe.svg)](https://asciinema.org/a/xnHSAucq78OOxHAe)

**brain-prime**  
[![asciicast](https://asciinema.org/a/mrJ7TooBXbpvF1Xb.svg)](https://asciinema.org/a/mrJ7TooBXbpvF1Xb)

**brain-calc**  
[![asciicast](https://asciinema.org/a/pqh6YWCsJdUUMcmu.svg)](https://asciinema.org/a/pqh6YWCsJdUUMcmu)
```