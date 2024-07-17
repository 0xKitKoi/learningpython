#from pyautogui import *
import pyautogui
import keyboard
import pyscreenshot
#import numpy as np
#import cv2
#import time
#import random
#import time
import mouse

def clicK(x, y):
    mouse.move(x, y, absolute=True)
    pyautogui.click()

while keyboard.is_pressed('q') == False:
    if pyscreenshot.grab().getpixel((557, 457))[0] == 17:
        clicK(557, 457)
    if pyscreenshot.grab().getpixel((662, 457))[0] == 17:
        clicK(662, 457)
    if pyscreenshot.grab().getpixel((760, 457))[0] == 17:
        clicK(760, 457)
    if pyscreenshot.grab().getpixel((856, 457))[0] == 17:
        clicK(856, 457)
