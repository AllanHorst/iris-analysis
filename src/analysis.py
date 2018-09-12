import numpy
import cv2

def apply(img):
  for i in range(0, len(img)):
    for j in range(0, len(img[i])):
      print(img[i][j])