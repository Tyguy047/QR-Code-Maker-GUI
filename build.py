import subprocess as sp
import sys

# Removed "--onefile" to improve startup speed
sp.run(["pyinstaller", "--windowed", "--name", "QR Code Generator", "--icon=icon.png", "main.py"])