import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# # 1. Paint the image with a certain color
# blank[200:300, 300:400] = 255, 0, 255
# cv.imshow('Green', blank)
# 
# # 2. Draw a rectangle
# cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)
# 
# # 3. Draw a circle
# cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 50, (0, 0, 255), thickness=-1)
# cv.imshow('Circle', blank)
# 
# # 4. Draw a line
# cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=2)
# cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Louis', (10, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)
