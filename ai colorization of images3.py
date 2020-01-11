# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:11:33 2020

@author: Muhammad
"""

import cv2
import numpy as np
import matplotlib.pyplot as pIt
a=cv2.imread("IMAGE3.jpg")
pIt.imshow(a)
img=cv2.cvtcolor(a,cv2.COLOR_GRAY2BGR)
cv.imwrite("IMAGE3.jpg",a)