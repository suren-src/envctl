import subprocess

from utils.formatter import print_status

# def run_command(cmd) -> str:
#    try:
#        print_status(f"running command {cmd}")
#        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
#        return result.stdout
#    except subprocess.CalledProcessError as e:
#        return f"Error: {e.stderr}"
   
def run_command(cmd) -> tuple[bool, str, str]:
   """Run a shell command and return its status and output."""
   try:
       print_status(f"running command {cmd}")
       result = subprocess.run(cmd, capture_output=True, text=True)
       success = result.returncode == 0
       
       # For brew specifically, warnings appear in stderr but aren't failures
       if cmd[0] == "brew" and result.stderr and "Warning" in result.stderr:
           return True, result.stdout, result.stderr
           
       return success, result.stdout, result.stderr
   except Exception as e:
       return False, "", str(e)