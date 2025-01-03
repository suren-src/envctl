# envctl

## Prerequisites 

- Brew (for macOS)
- Python
- `uv` package manager
- `zsh` 

## Example of using another shell

```
- `fish` 
# Using fish as a default shell
echo $(which fish) | sudo tee -a /etc/shells
chsh -s $(which fish)
# log out
echo $SHELL

```
## From terminal

```
uv run ruff check
uv run envctl.py mac sync
```

## using venv

```
uv venv
source .venv/bin/activate
uv sync
python main.py
```



see: https://docs.astral.sh/uv/guides/projects/#managing-dependenciesu
