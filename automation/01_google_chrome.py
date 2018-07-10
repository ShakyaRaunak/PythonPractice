import os
import subprocess

# METHOD 1 :
# CHROME_HOME = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

# It is always nice to use os.path.join, even if your code is platform-specific at this point.
# CHROME_HOME = os.path.join('C:\\', 'Program Files (x86)', 'Google', 'Chrome', 'Application', 'chrome.exe')

# Make sure you're not running another copy of Chrome
# os.system('taskkill /f /im chrome.exe')  # /f to enforce kill task forcefully

# subprocess.call([CHROME_HOME, '--fullscreen'])

"""
Also try this :
subprocess.call([CHROME, '--kiosk'])
# It appears that Chrome will only start in Kiosk mode if no other instances are running.
"""

# METHOD 2 :
# https://docs.python.org/3/library/webbrowser.html
import webbrowser

# GOOGLE_HOME = "http://www.google.com/"
# webbrowser.open_new_tab(GOOGLE_HOME)c

# METHOD 3 :
# CHROME_HOME = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# webbrowser.get(CHROME_HOME).open_new(GOOGLE_HOME)


# import time

file = open('websites.txt', 'r')
websites = file.read().splitlines()

for url in websites:
    webbrowser.open_new_tab(url)
    # time.sleep(5)

# PyInstaller execution commands to convert Python scripts into standalone application :
# $ cd C:\Users\rauna\Desktop\PythonPractice\automation
# $ C:\ProgramData\Anaconda3\Scripts\pyinstaller.exe --onefile 01_google_chrome.py
# OR
# $ C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\Scripts\pyinstaller-script.py --onefile 01_google_chrome.py

"""
Notice that we passed an argument “-- onefile”; this creates a standalone executable in the dist directory of your 
script folder. This argument tells PyInstaller to create only one file. If you don’t specify this, 
the libraries will be distributed as separate file along with the executable.
"""
