import cv2
import numpy as np

def four_pieces(imgs):
  pieces = { "0": first, "1": second, "2": third, "3": fourth }
  for i in range(0, len(imgs)):
    crop = pieces.get(str(i))(imgs[i])
    # cv2.imshow('crop'+str(i), crop)
verificar angulos
def first(img):
  rows,cols = img.shape
  M = cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1)
  dst = cv2.warpAffine(img, M, (cols,rows))
  croped_img = dst[23:71, 15:100]
  return croped_img

def second(img):
  rows,cols = img.shape
  M = cv2.getRotationMatrix2D((cols/2,rows/2), -45, 1)
  dst = cv2.warpAffine(img,M,(cols,rows))
  croped_img = dst[25:71, 15:100]
  cv2.imshow('crop', croped_img)
  cv2.imshow('img', dst)
  return croped_img

def third(img):
  rows,cols = img.shape
  M = cv2.getRotationMatrix2D((cols/2,rows/2), -45, 1)
  dst = cv2.warpAffine(img,M,(cols,rows))
  croped_img = dst[47:80, 15:100]
  return croped_img

def fourth(img):
  rows,cols = img.shape
  M = cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1)
  dst = cv2.warpAffine(img,M,(cols,rows))
  croped_img = dst[25:71, 15:100]
  return croped_img