import ctypes

test = ctypes.CDLL("/home/kitkoi/pyImageRecog/clicktesting.so")

test.mouseClick(1)
