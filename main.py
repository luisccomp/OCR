import cv2 as cv
import easyocr
import matplotlib.pyplot as plt
from core.utils import string_utils


def rescale_image(image, scale=0.75):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)

    dimensions = width, height

    return cv.resize(image, dimensions, interpolation=cv.INTER_CUBIC)

IMG_PATH = 'images/cnh_full.jpg'


img = cv.imread(IMG_PATH)

gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
gray = cv.bitwise_not(gray)

# cv.imshow('TH', thresh)

# cv.imshow('RG', gray)

reader = easyocr.Reader(['en', 'pt', 'la'], gpu=False)
result = reader.readtext(gray, width_ths=0.85, height_ths=1.0, paragraph=True)

for r in result:
    print(r)

result = list(map(lambda x: (x[0], string_utils.remove_accents(x[1]), x[2]), result))

for detection in result:
    top_left = tuple(int(val) for val in detection[0][0])
    bottom_right = tuple(int(val) for val in detection[0][2])
    text = detection[1].upper().strip()
    font = cv.FONT_HERSHEY_SIMPLEX
    img = cv.rectangle(img, top_left, bottom_right, (255, 0, 0), 1)
    img = cv.putText(img, text, top_left, font, 0.5, (0, 0, 0), 2, cv.LINE_AA)

for detection in result:
    print(detection)

plt.imshow(img)
plt.show()

# cv.imshow('IMG', gray)

cv.waitKey(0)

# from difflib import SequenceMatcher
# 
# matces = [
#     lambda x: SequenceMatcher(a='VALIDA EM TODO O TERRITORIO NACIONAL', b=x.upper()).ratio(),
#     lambda x: SequenceMatcher(a='REGISTRO', b=x.upper()).ratio(),
#     lambda x: SequenceMatcher(a='DATA DE', b=x.upper()).ratio(),
#     lambda x: SequenceMatcher(a='REGISTRO', b=x.upper()).ratio()
# ]
