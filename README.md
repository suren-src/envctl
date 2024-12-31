# envctl

## Prerequisites 

- Brew (for macOS)
- Python
- `uv` package manager
- `zsh` (only if not installed)

## From terminal

```
uv run ruff check
uv run envctl.py mac
```

## using venv

```
uv venv
source .venv/bin/activate
uv sync
python main.py
```

see: https://docs.astral.sh/uv/guides/projects/#managing-dependenciesu
