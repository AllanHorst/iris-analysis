import numpy as np
import cv2

def threshold(gray):
  ret, th1 = cv2.threshold(gray, 255, 255, cv2.THRESH_TRUNC)
  return th1

def range_list(my_range):
  my_list = list(range(256))
  return [my_list[i:i+my_range] for i in range(0, len(my_list), my_range)]

def check_color(px, my_range, my_list):
  min_value = my_list[0]
  max_value = my_list[my_range -1]
  if (min_value >= px and px <= max_value):
    return max_value

  return None

def contrast(gray, my_range):
  ranges = range_list(my_range)

  for i in range(0, len(gray)):
    for j in range(0, len(gray[i])):

      for k in range(0, len(ranges)):
        new_color = check_color(gray[i][j], my_range, ranges[k])
        if (new_color):
          gray[i][j] = new_color
          break

  return gray

img = cv2.imread('images/with_diabetes/3esim.png')
img = cv2.resize(img, (720, 576))
original_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('original_gray', original_gray)
np.savetxt('text1.txt',original_gray,fmt='%.2f')
gray = contrast(original_gray, 16)
np.savetxt('text2.txt',gray,fmt='%.2f')
cv2.imshow('th1', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
