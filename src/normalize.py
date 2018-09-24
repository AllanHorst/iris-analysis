import cv2
import numpy as np

img = None
center = None

def four_pieces(img_param, center_param):
  global img
  img = img_param
  global center
  center = center_param

  horizontally = int(center[0] * 0.60182)
  vertically = int(center[1] * 0.60182 )
  print('center x:' + str(center[0]))
  print('center y:' + str(center[1]))
  print(horizontally)
  print(vertically)
  print(center[2])
  cv2.circle(img, (horizontally, vertically), 2, (0, 0, 255), 3)



# def first(radius, img):
