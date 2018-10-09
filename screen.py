import os
from PIL import ImageGrab

IMAGE_DIR = "screenshot.png"

def shot():
    # (x0,y0,x1,y1) need two points to create rectangle
    img = ImageGrab.grab(bbox=[20,200,420,800])
    img.save(IMAGE_DIR)