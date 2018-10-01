import numpy as np
import cv2

img = cv2.imread('images/without_diabetes/3d.png', 0)
blank = np.zeros((256, 256))
hist = cv2.calcHist([img],[0],None,[256],[0,255])
for x,y in enumerate(hist):
  cv2.line(blank, (x, 0), (x, y), (255, 255, 255))

cv2.imshow('a', blank)

cv2.imshow('or', img)
cv2.waitKey(0)
cv2.destroyAllWindows