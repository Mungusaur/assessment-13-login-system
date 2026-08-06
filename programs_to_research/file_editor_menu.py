import os
import sys
import subprocess
from pathlib import Path

dir_path = Path(__file__).resolve().parent

def open_in_default_editor(filepath):
    # Ensure the file exists before opening
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        return

    # Windows platform
    if sys.platform == "win32":
        os.startfile(filepath)
        
    # macOS platform
    elif sys.platform == "darwin":
        subprocess.Popen(["open", filepath])
        
    # Linux and Unix-like platforms
    else:
        subprocess.Popen(["xdg-open", filepath])

# Example usage:
file_to_open = str(dir_path)+r"\example.txt"
open_in_default_editor(file_to_open)
