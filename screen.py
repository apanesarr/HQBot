import os
import json
from PIL import ImageGrab

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
IMAGE_DIR = data["LOCAL"]["IMAGE_PATH"]

def shot():
    # (x0,y0,x1,y1) need two points to create rectangle
    # make sure screenshot.png only contains question 
    img = ImageGrab.grab(bbox=[20,200,420,800])
    img.save(IMAGE_DIR)