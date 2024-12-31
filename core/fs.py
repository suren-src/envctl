from pathlib import Path
from core.logger import logger

def ensure_directory(path):
   full_path = Path.home() / path
   
   if full_path.exists():
       logger.info(f"✓ Directory found {full_path}")
       return str(full_path)
       
   try:
       full_path.mkdir(parents=True, exist_ok=True)
       logger.info(f"✓ Directory created {full_path}")
       return str(full_path)
   except Exception as e:
       logger.error(f"❌ Error: {e}")