@echo off
pyinstaller --noconfirm --onefile --windowed --icon "main.ico" --name "mcb-video-utils"  "main.py"
REM OR USE auto-py-to-exe