import numpy as np
import cv2

min_area = 50
max_area = 800
a = 50
b = 250
c = 500
d = 800

def draw_countour(img, cnt):
  rect = cv2.minAreaRect(cnt)
  box = cv2.boxPoints(rect)
  box = np.int0(box)
  cv2.drawContours(img,[box],0,(0,0,255),1)

def fuzzify(avarage):
  calc1 = (avarage - a) / (b - a)
  calc2 = (d - avarage) / (d - c)
  result = max(min(calc1, 1, calc2), 0)
  return result * 100

def analyze(img):
  print('#' * 20)
  th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY_INV, 41, 3)


  im2, contours, hierarchy = cv2.findContours(th3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sum_area = 0
  count = 0
  for i in range(0, len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    print('area: ', area)
    if (area > min_area and area < max_area):
      sum_area += area
      count += 1
      draw_countour(img, cnt)
      break

  avarage = sum_area / count
  print('sum area: ', sum_area)
  print('fuzzy result: ', fuzzify(avarage))
  print('contours: ', len(contours))
  return fuzzify(avarage), img

