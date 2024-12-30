from pathlib import Path
from utils.formatter import print_status

def ensure_directory(path):
   full_path = Path.home() / path
   
   if full_path.exists():
       print_status("Directory found", full_path, "success")
       return str(full_path)
       
   try:
       full_path.mkdir(parents=True, exist_ok=True)
       print_status("Directory created", full_path)
       return str(full_path)
   except Exception as e:
       print_status(f"Error: {str(e)}", full_path, "error")