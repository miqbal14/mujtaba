# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:40:46 2020

@author: Muhammad
"""

import cv2
import numpy
img=cv2.imread('1.jpg')
ret,gray = cv2.threshold(img,127,256,cv2.THRESH_BINARY)
cv2.imshow('Orginal image',img)
cv2.imshow('Binary Image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
