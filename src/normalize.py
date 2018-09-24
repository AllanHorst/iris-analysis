import cv2
import numpy as np
import divider

img = None
center = None

def four_pieces(img_param, center_param):
  global img
  img = img_param
  global center
  center = center_param
  height,width = img.shape
  x = center[0]
  r = center[2] * 3
  y = center[1]
  # cir= cv2.circle(mask, (center[0], center[1]), int(center[2] * 3.5), (0, 0, 255), thickness=-1)
  crop_img = img[y-r:y+r, x-r:x+r]
  cv2.resize(crop_img, (360, 288))
  imgs, img = divider.apply(crop_img)

  test = imgs[0]
  rows,cols = test.shape

  M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
  dst = cv2.warpAffine(test,M,(cols,rows))
  croped_img = dst[25:71, 18:90]
  cv2.imshow('ass', croped_img)
  cv2.imshow('as', dst)

# def first(radius, img):
