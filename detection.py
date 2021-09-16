from matplotlib import pyplot as plt
from numpy import ndarray
import cv2 as cv


def resize_image(image: ndarray, scale: float = 0.75) -> ndarray:
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)

    dimensions = width, height

    return cv.resize(image, dimensions, interpolation=cv.INTER_CUBIC)


IMAGE_PATH = 'images/cnh_full.jpg'

img = resize_image(cv.imread(IMAGE_PATH), scale=2.0)
img = cv.GaussianBlur(img, (3, 3), 127)

plt.imshow(img)
plt.show()
