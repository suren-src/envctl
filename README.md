# envctl

## Prerequisites 

- Brew (for macOS)
- Python
- `uv` package manager

## From terminal

```
uv run ruff check
uv run main.py
```

## using venv

```
uv venv
source .venv/bin/activate
uv sync
python main.py
```

see: https://docs.astral.sh/uv/guides/projects/#managing-dependenciesu
