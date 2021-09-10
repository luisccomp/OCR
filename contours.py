import cv2 as cv
import numpy as np

img = cv.imread('images/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny edges', canny)
# 
# contours, hierarchies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# 
# print(f'Contours: {len(contours)} found!')

ret, thresh = cv.threshold(gray, 125, 175, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours', blank)

print(f'Contours: {len(contours)} found!')

cv.waitKey(0)
