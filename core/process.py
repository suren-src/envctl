import subprocess
from core.logger import logger
   
def run_command(cmd) -> tuple[bool, str, str]:
   """Run a shell command and return its status and output."""
   try:
       logger.info(f"running: {' '.join(cmd)}")
       result = subprocess.run(cmd, capture_output=True, text=True)
       success = result.returncode == 0
       
       # For brew specifically, warnings appear in stderr but aren't failures
       if cmd[0] == "brew" and result.stderr and "Warning" in result.stderr:
           return True, result.stdout, result.stderr
           
       return success, result.stdout, result.stderr
   except Exception as e:
       return False, "", str(e)