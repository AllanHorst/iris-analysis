import numpy as np
import cv2

min_area = 100
max_area = 800

def draw_countour(img, cnt):
  rect = cv2.minAreaRect(cnt)
  box = cv2.boxPoints(rect)
  box = np.int0(box)
  cv2.drawContours(img,[box],0,(0,0,255),1)

def analyze(img):
  has_smudge = False
  th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY_INV, 41,3)

  for y in range(0, len(img)):
    for x in range(0, len(img[y])):
      if (th3[y][x] == 0):
        continue
      if (img[y][x] < 100):
        th3[y][x] = 255


  im2, contours, hierarchy = cv2.findContours(th3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  for i in range(0, len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    print(area)
    if (area > min_area and area < max_area):
      has_smudge = True
      break


  print(has_smudge)
  return has_smudge

  # cv2.imshow('th3', th3)
  # cv2.imshow('img', img)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()