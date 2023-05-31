import pyautogui
import pyperclip

position = pyautogui.position()
print(position)

pyautogui.doubleClick(132, 200)

pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")

text = pyperclip.paste()
print(text)
