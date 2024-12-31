import typer

from core.boostrap import backup_configs
from core.fs import ensure_directory
from brew import install
from core.logger import logger

cli = typer.Typer()
mac_app = typer.Typer()
cli.add_typer(mac_app, name="mac")

@mac_app.command("sync")
def sync():
    install.install()

if __name__ == "__main__":   
    try:
        logger.info('Starting...')
        #cli()
        ensure_directory('.envctl')
        backup_configs()
        install.install()
    except Exception as e:
        logger.error(f'Error during Execution: {e}', exc_info=True)
    

