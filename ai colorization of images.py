# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:51:49 2020

@author: Muhammad
"""

import cv2
import numpy as np
import matplotlib.pyplot as pIt
a=cv2.imread("IMAGE.jpg")
pIt.imshow(a)
img=cv2.cvtcolor(a,cv2.COLOR_GRAY2BGR)
cv.imwrite("IMAGE.jpg",a)