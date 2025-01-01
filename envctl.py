from datetime import time
import typer
import brew
import config_manager.copier
import core
import config_manager
from core.logger import logger
import ide

cli = typer.Typer()
mac_app = typer.Typer()
cli.add_typer(mac_app, name="mac")

@mac_app.command("sync")
def sync(
        items: str = typer.Option("all", "--items", "-i", 
                        help="What to sync: all,config,tools,nvim,vscode (comma-separated)"),
        backup: bool = typer.Option(True, "--backup/--no-backup", "-b/-nb", 
                        help="Whether to backup existing configs before sync")
    ):
    try:
        sync_items = core.utils.validate_sync_items(items)
        logger.info(f"Starting sync for: {', '.join(sync_items)}")
        
        if backup:
            logger.info("Backing up existing configs")
            core.backup_configs()
        else:
            logger.info("Skipping backup")
                
        if "tools" in sync_items:
            brew.install()
            
        if "config" in sync_items:
            config_manager.Copier().copy()
        
        if "nvim" in sync_items:
            ide.Nvim().setup()

        if "vscode" in sync_items:
            ide.Vscode().setup()
            
        if "all" in sync_items:
            brew.install()
            config_manager.Copier().copy()
            ide.Nvim().setup()
            ide.Vscode().setup()
        
        logger.info("Sync completed successfully")
            
    except Exception as e:
        logger.error(f"Error during sync: {e}", exc_info=True)
        raise typer.Exit(1)

if __name__ == "__main__":
    try:
        logger.info("Starting...")
        core.ensure_directory(".envctl")
        core.ensure_directory(".config")
        cli()
    except Exception as e:
        logger.error(f"Error during execution: {e}", exc_info=True)
        raise typer.Exit(1)