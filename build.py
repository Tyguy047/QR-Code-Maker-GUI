import subprocess as sp

windows = input("Are you using Windows? (Y/N)")

# The --onefile flag is only used for Windows since Mac OS and Linux systems will automatically turn the final build into a single standalone excutable.
# Using --onefile used on Mac OS and Linux systems will result in slow and sometimes buggy startups.
if windows.lower() == 'y':
    sp.run(["pyinstaller", "--windowed", "--onefile", "--name", "QR Code Generator", "--icon=icon.png", "main.py"])

else:
    sp.run(["pyinstaller", "--windowed", "--name", "QR Code Maker", "--icon=icon.png", "main.py"])

print("Your executable can be found in the dist folder")