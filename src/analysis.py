import numpy as np
import cv2

min_area = 50
medium_area = 300
max_area = 600

def draw_countour(img, cnt):
  rect = cv2.minAreaRect(cnt)
  box = cv2.boxPoints(rect)
  box = np.int0(box)
  cv2.drawContours(img,[box],0,(0,0,255),1)

def fuzzify(avarage):
  calc1 = (avarage - min_area) / (medium_area - min_area)
  calc2 = (max_area - avarage) / (max_area - medium_area)
  return max(min(calc1, calc2), 0)

def analyze(img):
  th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY_INV, 41, 4)


  im2, contours, hierarchy = cv2.findContours(th3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sum_area = 0
  count = 0
  for i in range(0, len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    if (area > min_area and area < max_area):
      sum_area += area
      count += 1
      draw_countour(img, cnt)
      break

  avarage = sum_area / count
  return fuzzify(avarage), img

