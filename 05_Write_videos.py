# When each frame is read, a new parameter holds the read frame in a flip mode
# and writes the flipped frame into another video file.

import cv2
import numpy as np 

vid = cv2.VideoCapture("./data/sample.mp4")

fcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("./data/new_sample.avi", fcc, 28, (640, 360))

while True:
    ret, f = vid.read()
    f2 = cv2.flip(f, 1)
    
    cv2.imshow("frame2", f2)
    cv2.imshow("frame", f)

    out.write(f2)

    key = cv2.waitKey(20)
    if key == 27:
        break

    
out.release()
vid.release()
cv2.destroyAllWindows()