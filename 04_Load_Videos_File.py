import cv2
import numpy as np 

vid = cv2.VideoCapture("./data/shore.mov")

while True:
    ret, frame = vid.read()
    cv2.imshow("frame", frame)

    key = cv2.waitKey(25)
    if key == 27:
        break

vid.release()
cv2.destroyAllWindows()