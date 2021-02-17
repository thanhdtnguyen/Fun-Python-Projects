import pyautogui
import time

pyautogui.FAILSAFE = False

while True:
    time.sleep(100)
    for i in range(50, 100):
        pyautogui.moveTo(0, i*5)
    for i in range(0, 3):
        pyautogui.press('shift')