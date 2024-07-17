import numpy as np
import pyscreenshot as ImageGrab
import time
import cv2


smallerGameCoords = [657, 800, 1262, 802]

screen = np.array(ImageGrab.grab(bbox=smallerGameCoords))
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

ImageGrab.show()
#ImageGrab.save("test.png")
