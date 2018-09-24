import cv2
import numpy as np

def four_pieces(imgs):
  test = imgs[0]
  rows,cols = test.shape
  M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
  dst = cv2.warpAffine(test,M,(cols,rows))
  croped_img = dst[25:71, 18:90]
  cv2.imshow('ass', croped_img)
