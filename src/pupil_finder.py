import cv2
import divider
import numpy as np

def find(img):
  img = cv2.medianBlur(img, 5)
  cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

  circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100,
                              param1=50, param2=30, minRadius=0, maxRadius=50)
  if (circles is None or len(circles[0]) > 1):
    return None

  circles = np.uint16(np.around(circles))
  center = circles[0][0]
  x = center[0]
  r = center[2] * 3
  y = center[1]

  crop_img = img[y-r:y+r, x-r:x+r]
  cv2.resize(crop_img, (180, 180))

  imgs, img2 = divider.apply(crop_img)
  return imgs