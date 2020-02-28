import numpy as np 
import cv2

panda_img = cv2.imread("./data/pandas.jpg")
panda_gray_img = cv2.cvtColor(panda_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Color Panda", panda_img)
cv2.imshow("Grey Panda", panda_gray_img)
cv2.imwrite("./data/gray_panda.jpg", panda_gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()