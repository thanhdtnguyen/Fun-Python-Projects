import os
import pyautogui
import time
from datetime import datetime

now = datetime.now()
print(now)

h = now.hour
m = now.minute

if h == 15:
    if 20 < m < 26:
        os.system('open /Applications/zoom.us.app')
        time.sleep(3)

        pyautogui.click(x=513, y=300)
        pyautogui.PAUSE = 3

        meetingID = '2359639412'

        pyautogui.typewrite(meetingID)

        pyautogui.click(x=776, y=518)