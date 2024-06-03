import time
import os
import codecs
import csv
import pandas as pd
import numpy as np
import glob
import math

from PIL import Image
from pytesseract import pytesseract
import cv2

def get_searchbar_text_from_image(fn):
    text = ""
    if os.path.exists(fn):
        try:
            img = Image.open(fn)
            box = (2012,85,2350,150)# box for the entire search bar
            img_crop =  img.crop(box)
            # img_crop.show()
    
            text1 = pytesseract.image_to_string(img_crop)
            print(text1)
          
            box = (2290,85,2350,150)
            img_crop =  img.crop(box)
            # img_crop.show()
            text = pytesseract.image_to_string(img_crop)
        except:
            print("error")
           
    return text
    


folder_image = # add some folder path containing the images

for fn in glob.glob(folder_image+"*.png"):
    print(fn)
    text = get_searchbar_text_from_image(fn)
    print(text)
    print(" ")
    
