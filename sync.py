import typer

from utils.fs import ensure_directory
from brew import install

cli = typer.Typer()
mac_app = typer.Typer()
cli.add_typer(mac_app, name="mac")

@mac_app.command("sync")
def sync():
    install.install()

if __name__ == "__main__":
    #cli()
    install.install()
    result = ensure_directory('.backup')