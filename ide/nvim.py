import shutil
from pathlib import Path
from core.logger import logger

class Nvim:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.src_dir = self.base_dir / "nvim"
        
        if not self.src_dir.exists():
            raise FileNotFoundError(f"Files directory not found: {self.src_dir}")

    def ensure_dir_exists(self, path: Path) -> None:
        if not path.exists():
            path.mkdir(parents=True)
            logger.debug(f"Created directory: {path}")

    def copy_handler(self, src_path: str, dst_path: str):
        dst_path = Path(dst_path)  # Convert string to Path
        if dst_path.exists():
            logger.info(f"Overwriting existing file: {dst_path}")
        return shutil.copy2(src_path, dst_path)  

    def setup(self) -> None:
        try:
            src: Path = self.src_dir 
            dst: Path = Path.home() / ".config" / "nvim"

            shutil.copytree(src, dst, copy_function=self.copy_handler, dirs_exist_ok=True)
            logger.info("nvim config setup completed successfully")

        except Exception as e:
            logger.error(f"Error during copy operation: {str(e)}")
            raise
