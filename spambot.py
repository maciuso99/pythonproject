
import pyautogui
import time

def sendSpamBot():
    time.sleep(5)

    text = "Siema to jest napad na ten kanal discord"
    while True:
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        time.sleep(0.8)

sendSpamBot()

