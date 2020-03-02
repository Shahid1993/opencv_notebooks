import numpy
import cv2

img = cv2.imread("./data/SnP_noise.jpg")

# kernel of 5*5 matrix neighbourhood is used
noisereduced_version = cv2.medianBlur(img, 5)

cv2.imshow("original", img)
cv2.imshow("corrected", noisereduced_version)

cv2.waitKey(0)