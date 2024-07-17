import numpy as np
import pyscreenshot as ImageGrab
import cv2


gameCoords = "10, 20, 100, 300"

#screen = np.array(ImageGrab.grab(bbox=smallerGameCoords))
#screen = np.array(ImageGrab.grab(bbox=map(int, gameCoords.split(', '))))

#screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
ImageGrab.grab_to_file('image.png')

