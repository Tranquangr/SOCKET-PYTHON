import pyautogui
from PIL import Image
myScreenshot=pyautogui.screenshot()
myScreenshot.save("111.png")
im = Image.open("111.png")
im.show()