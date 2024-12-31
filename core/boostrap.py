from pathlib import Path
import shutil
from datetime import datetime
from core.logger import logger

_default_config_paths = [
    "~/.config",  # dir
    "~/.zshrc",
    "~/.bashrc",
    "~/.zprofile",
    "~/.customrc",
    "~/.devrc",
    "~/.vimrc",
    "~/.tmux.conf",
]

def _ignore_sockets(src, names):
    """Function to identify socket files that should be ignored during copy"""
    return [
        name
        for name in names
        if Path(src, name).is_socket() or Path(src, name).is_fifo()
    ]


def backup_configs(backup_dir: str = ".envctl/backups", config_paths: list = None):
    """
    Backup config files to specified directory
    Args:
        backup_dir: directory to store backups (default: .envctl/backups)
        config_paths: list of paths to backup (default: common config files)
    """
    if config_paths is None:
        config_paths = _default_config_paths

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = Path.home() / backup_dir / timestamp
    backup_path.mkdir(parents=True, exist_ok=True)

    logger.info(f"Starting config backup to {backup_path}")

    backed_up = []
    skipped = []

    for config in config_paths:
        src = Path(config).expanduser()
        if not src.exists():
            logger.debug(f"Skipping {src} - does not exist")
            skipped.append(str(src))
            continue

        try:
            dest = backup_path / src.name
            if src.is_dir():
                logger.info(f"Backing up directory {src}")
                shutil.copytree(
                    src, dest, ignore=_ignore_sockets
                )  # Added ignore function
            else:
                logger.info(f"Backing up file {src}")
                shutil.copy2(src, dest)
            backed_up.append(str(src))
        except Exception as e:
            logger.error(f"Failed to backup {src}: {str(e)}")
            skipped.append(str(src))

    logger.info(f"Backed up {len(backed_up)} items. Skipped {len(skipped)} items.")
    logger.info(f"Backup created at: {backup_path}")

    return True
