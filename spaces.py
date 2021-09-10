import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/park.jpg')
cv.imshow('Boston', img)

# BGR to grayscale conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV conversion
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('Lab', lab)

# BGR to RGB conversion
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# hsv to BGR conversion
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

# Lab to BGR convertion
lab_bgr = cv.cvtColor(lab, cv.COLOR_Lab2BGR)
cv.imshow('Lab --> BGR', lab_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)
