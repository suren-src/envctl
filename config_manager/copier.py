import shutil
from pathlib import Path
from core.logger import logger

class Copier:
    def __init__(self):
        """Get the absolute path to the directory containing this script"""
        self.base_dir = Path(__file__).parent
        self.files_dir = self.base_dir / "files"
        
        if not self.files_dir.exists():
            raise FileNotFoundError(f"Files directory not found: {self.files_dir}")

    def ensure_dir_exists(self, path: Path) -> None:
        """Create directory if it doesn't exist."""
        if not path.exists():
            path.mkdir(parents=True)
            logger.debug(f"Created directory: {path}")

    def copy_with_parents(self, src: Path, dst: Path) -> None:
        """Copy file and create parent directories if needed."""
        self.ensure_dir_exists(dst.parent)
        shutil.copy2(src, dst)
        logger.debug(f"Copied: {src} -> {dst}")

    def copy(self) -> None:
        """Copy configuration files to their respective locations."""
        try:
            config_src = self.files_dir / "config"
            home = Path.home()
            config_dst = home / ".config"
            
            if not config_src.exists():
                logger.error("Source config directory not found")
                return
            
            file_mappings = {
                "customrc": ".customrc",
                "zprofile": ".zprofile",
                "zshrc": ".zshrc"
            }

            # Copy rc files
            for src_name, dst_name in file_mappings.items():
                src_path = self.files_dir / src_name
                if src_path.exists():
                    dst_path = home / dst_name
                    self.copy_with_parents(src_path, dst_path)
                else:
                    logger.warning(f"Source file not found: {src_path}")

            # Copy all files in config/ maintaining directory structure
            for src_path in config_src.rglob("*"):
                if src_path.is_file():
                    rel_path = src_path.relative_to(config_src)
                    dst_path = config_dst / rel_path
                    self.copy_with_parents(src_path, dst_path)

            logger.info("Copy completed successfully")

        except Exception as e:
            logger.error(f"Error during copy operation: {str(e)}")
            raise