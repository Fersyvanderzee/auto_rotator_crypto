import webbrowser
import pyautogui
from time import sleep

try:
    file = open("links.txt", "r")

except FileNotFoundError:
    print("File not found. Sure it is in the right directory?")

# open every link in links.txt in a separate tab
for f in file:
    webbrowser.open(f)

# wait for a couple of seconds so the keyboard input of f11 won't be missed by the browser
sleep(4)
pyautogui.press('f11')

# switch between tabs every 5 seconds
while(True):
    sleep(5)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('ctrl')


