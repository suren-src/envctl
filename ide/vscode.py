import shutil
import sys
from pathlib import Path
import core
from core.logger import logger
from ide.vscode_inventory import extensions, themes

"""
For Mac:
Settings & Keybindings:
~/Library/Application Support/Code/User/
- settings.json
- keybindings.json

Extensions:
~/.vscode/extensions/

Snippets:
~/Library/Application Support/Code/User/snippets/

Workspaces (if any):
~/Library/Application Support/Code/Workspaces/
"""

class Vscode:
    def __init__(self):
        # Check for 'code' command in PATH
        code_in_path = shutil.which("code") is not None
        if not code_in_path:
            raise FileNotFoundError("VS Code not found in Path")

        self.base_dir = Path(__file__).parent
        self.src_dir = self.base_dir / "vscode"

        if not self.src_dir.exists():
            raise FileNotFoundError(f"Files directory not found: {self.src_dir}")

        if core.SupportedPlatform.is_mac():
            vscode_path = Path.home() / "Library/Application Support/Code/User"
        elif core.SupportedPlatform.is_linux():
            vscode_path = Path.home() / ".config/Code/User"
        elif core.SupportedPlatform.is_windows():
            vscode_path = "%APPDATA%/Code/User"
        else:
            raise RuntimeError(f"Unsupported platform: {sys.platform}")
        
        self.vscode_path = vscode_path

    def setup(self) -> None:
        try:
            shutil.copy2(self.src_dir/"settings.json", self.vscode_path)

            if core.SupportedPlatform.is_mac():
                shutil.copy2(self.src_dir/"mac_keybindings.json", 
                             self.vscode_path/"keybindings.json")
            else:
                shutil.copy2(self.src_dir/"keybindings.json", 
                            self.vscode_path/"keybindings.json")

            shutil.copytree(self.src_dir/"snippets", 
                            self.vscode_path/"snippets", dirs_exist_ok=True)

            self.install_extensions()

            logger.info("vscode config setup completed successfully")

        except Exception as e:
            logger.error(f"Error during copy operation: {str(e)}")
            raise


    def install_extensions(self) -> None:
        logger.info("Installing VS Code Extensions")
        for extension in [ext.strip() for ext in extensions.splitlines() if ext.strip()]:
            res = core.process.run_command(["code", "--install-extension", extension, "--force"])
            logger.info(res)

        logger.info("Installing VS Code themes")
        for theme in [t.strip() for t in themes.splitlines() if t.strip()]:
            res = core.process.run_command(["code", "--install-extension", theme, "--force"])
            logger.info(res)
