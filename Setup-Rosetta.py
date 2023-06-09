#-------------------------------------------------------------------#
# BatchWhisper-Transcription-Translation [LOCAL & API]              #
#-------------------------------------------------------------------#
# Author: SABIAN HIBBS                                              #
# License: MIT                                                      #
# Version: 3.34                                                     #
#-------------------------------------------------------------------#

import subprocess
import time
import os

## More information found here: https://github.com/openai/whisper ##

if not os.path.exists('Input-Videos'):
    os.mkdir('Input-Videos')

def run(command):
    while True:
        result = subprocess.run(command, shell=True)
        if result.returncode == 0:
            return
        print(f"Command '{command}' failed. Retrying in 10 seconds...")
        time.sleep(10)

# Upgrade openai-whisper
run("pip install -U openai-whisper")

# Install whisper from GitHub
run("pip install git+https://github.com/openai/whisper.git")

# Upgrade whisper from GitHub
run("pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git")

# Install ffmpeg
run("pip install ffmpeg")

# Install openai
run("pip install openai")

# Install setuptools-rust
run("pip install setuptools-rust")

# Install torch for CUDA
run("pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117")
