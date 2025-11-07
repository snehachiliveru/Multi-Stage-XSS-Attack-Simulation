@echo off
echo Creating Python venv and installing requirements...
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
echo Setup done.
pause
