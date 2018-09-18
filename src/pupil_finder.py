import cv2
import numpy as np

def find(img):
  img = cv2.medianBlur(img, 5)
  cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

  circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100,
                              param1=50, param2=30, minRadius=0, maxRadius=50)

  if (circles is None or len(circles[0]) > 1):
    return None

  circles = np.uint16(np.around(circles))
  i = circles[0][0]
  return i[0], i[1]