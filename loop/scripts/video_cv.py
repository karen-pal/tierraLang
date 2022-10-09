import numpy as np
import cv2 as cv
import time

WINDOW_NAME = "visualz"
cv.namedWindow(WINDOW_NAME, cv.WND_PROP_FULLSCREEN)

cv.setWindowProperty(WINDOW_NAME, cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
cap = cv.VideoCapture('videos/hydra_short.mp4')
fps = cap.set(cv.CAP_PROP_FPS, 25)
fps_limit = 1
start = time.time()
while cap.isOpened():
    now = time.time()
    if (int(now - start) ) > fps_limit :
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv.imshow(WINDOW_NAME, frame)
        if cv.waitKey(1) == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
