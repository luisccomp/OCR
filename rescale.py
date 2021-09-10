import cv2 as cv


def rescale_frame(frame, scale=0.75):
    # Works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = width, height

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_res(capture, width, height):
    # Works for live videos only
    capture.set(3, width)
    capture.set(4, height)


img = cv.imread("images/cat.jpg")

resized_img = rescale_frame(img)

cv.imshow("Cat", img)
cv.imshow("Cat resized", resized_img)

# Reading videos
capture = cv.VideoCapture("videos/dog.mp4")
done = False

while True:
    is_true, frame = capture.read()

    if not is_true:
        break

    frame_resized = rescale_frame(frame)

    cv.imshow("Dog", frame)
    cv.imshow("Dog resized", frame_resized)
    cv.waitKey(20)

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
