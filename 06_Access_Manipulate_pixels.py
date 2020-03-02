import numpy
import cv2

flower_img = cv2.imread("./data/flower_pink.jpg")

pixel = flower_img[200, 250]

print(pixel)

# Change the pixel color value to blue
flower_img[300, 250] = (255, 0, 0)

# Change the pixel color value to green in a region range
flower_img[200:250, 200:350] = (0, 255, 0)

cv2.imshow("modified_pixel", flower_img)
cv2.waitKey(0)