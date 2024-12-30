from rich.console import Console
from rich.text import Text

console = Console()

def print_status(message, path="", status="info"):
   styles = {
       "success": ("green", "✓"),
       "info": ("yellow", "✨"),
       "error": ("red", "❌")
   }
   color, icon = styles.get(status, styles["info"])
   
   text = Text(f"{icon} {message}\n", style=f"bold {color}")
   #text.append(f"Location: {path}", style="blue")
   console.print(text)