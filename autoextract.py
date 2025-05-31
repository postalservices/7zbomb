import os
import subprocess
from pathlib import Path

def extract_recursive(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".7z"):
                file_path = os.path.join(root, file)
                extract_dir = os.path.splitext(file_path)[0]
                os.makedirs(extract_dir, exist_ok=True)
                subprocess.run(["7z", "x", file_path, f"-o{extract_dir}"])
                extract_recursive(extract_dir)

extract_recursive(".")
