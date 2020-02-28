import numpy as np 
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread("./data/pandas.jpg")

# plot histogram
hist_img = cv2.calcHist([img], [0], None, [900], [0,900])

# flatten the histogram
plt.hist(hist_img.ravel(), 900, [0, 900])
plt.show()

# view color channels
color = ['b', 'g', 'r']

# separate the colors and plot the histogram
for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [900], [0, 900])
    plt.plot(hist, color = col)
    plt.xlim(0,900)

plt.show()