import cv2 as cv

# Reading images using opencv and show it on screen
# img = cv.imread("images/cat_large.jpg")

# cv.imshow("Cat", img)

# Reading videos
capture = cv.VideoCapture("videos/dog.mp4")
done = False

while True:
    is_true, frame = capture.read()

    if not is_true:
        break

    cv.imshow("Dog", frame)
    cv.waitKey(20)

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
