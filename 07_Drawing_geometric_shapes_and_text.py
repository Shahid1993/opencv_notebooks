import numpy
import cv2

img = cv2.imread("./data/tree.jpg")

cv2.line(img, (200,200), (500,500), (255,0,0), 5)
cv2.rectangle(img, (200,200), (500,500), (0,255,0), 5)
cv2.circle(img, (350,350), 150, (0,0,255), 3) 

cv2.ellipse(img, (350,350), (150,50), 0, 0, 360, (100,0,0),3)

cv2.putText(img, "Writing text with openCV", (200,550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA )

cv2.imshow("geometry", img)
cv2.waitKey(0)