import cv2 as cv
import numpy as np


def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = img.shape[1], img.shape[0]

    return cv.warpAffine(img, trans_mat, dimensions)


def rotate(img, angle, rot_point=None):
    height, width = img.shape[:2]

    if not rot_point:
        rot_point = (width // 2, height // 2)

    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = width, height

    return cv.warpAffine(img, rot_mat, dimensions)


img = cv.imread('images/park.jpg')
cv.imshow('Boston', img)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

# Translation
translated = translate(img, -100, 100)
cv.imshow("Translated", translated)

# Rotation
rotated = rotate(img, -45)
cv.imshow("Rotated", rotated)

rotated_rotated = rotate(rotated, 45)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow("Flipped", flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
