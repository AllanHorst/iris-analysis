import cv2
import numpy as np

def four_pieces(imgs, radius):
  functions = { "0": first, "1": second, "2": third, "3": fourth }
  pieces = []
  for i in range(0, len(imgs)):
    crop = functions.get(str(i))(imgs[i])
    pieces.append(crop)
    # cv2.imshow('dst', dst)
    # cv2.imshow('img', imgs[i])
    # cv2.imshow('crop', crop)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

  return pieces

def first(img):
  rows,cols = img.shape
  M = cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1)
  dst = cv2.warpAffine(img, M, (cols,rows))
  croped_img = dst[30:60, 35:85]
  return croped_img

def second(img):
  rows,cols = img.shape
  M = cv2.getRotationMatrix2D((cols/2,rows/2), -45, 1)
  dst = cv2.warpAffine(img,M,(cols,rows))
  croped_img = dst[30:60, 19:78]
  return croped_img

def third(img):
  rows,cols = img.shape
  M = cv2.getRotationMatrix2D((cols/2,rows/2), -45, 1)
  dst = cv2.warpAffine(img,M,(cols,rows))
  croped_img = dst[30:60, 35:85]
  return croped_img

def fourth(img):
  rows,cols = img.shape
  M = cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1)
  dst = cv2.warpAffine(img,M,(cols,rows))
  croped_img = dst[30:60, 19:78]
  return croped_img