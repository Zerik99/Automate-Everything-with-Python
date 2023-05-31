import pyautogui
import time

position = pyautogui.position()
print(position)

pyautogui.doubleClick(132, 200)

time.sleep(2)
pyautogui.press("down")
pyautogui.press("enter")
pyautogui.write("Hello world!\n", interval=0.25)

pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")
pyautogui.press(5 * ["down"])
pyautogui.hotkey("ctrl", "v")
