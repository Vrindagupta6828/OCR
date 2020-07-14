# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:44:24 2020

@author: Lenovo
"""

import pytesseract
from PIL import Image
import cv2
import numpy as np

file_path= 'receipt.png'
im = Image.open(file_path)
im.save('ocr.png', dpi=(300, 300))

#binary threshold
image = cv2.imread('ocr.png')
image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
retval, threshold = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

text = pytesseract.image_to_string(threshold)

with open("Output.txt", "w",5 ,"utf-8") as text_file:
    text_file.write(text)