import pyautogui
import keyboard
import pyscreenshot

cords = pyscreenshot.grab(bbox=(530, 200, 875, 630))

def clicK(x, y):
    pyautogui.click(x, y)

while keyboard.is_pressed('q') == False:
    if cords.getpixel((33, 344))[0] == 17:
        clicK(557, 457)
    elif cords.getpixel((132, 327))[0] == 17:
        clicK(662, 457)
    elif cords.getpixel((235, 336))[0] == 17:
        clicK(760, 457)
    elif cords.getpixel((325, 339))[0] == 17:
        clicK(856, 457)

