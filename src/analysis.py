import numpy as np
import cv2
import contrast

def analyze(img):
  print(img)
  th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY, 31,2)
  # contrast.apply(img, 8)
  hist = cv2.calcHist([img],[0],None,[256],[0,255])

  blank = np.zeros((256, 256))

  for x,y in enumerate(hist):
    print(x, y)
    cv2.line(blank, (x, 0), (x, y), (255, 255, 255))

  cv2.imshow('a', blank)

  cv2.imshow('or', img)
  # cv2.imshow('img', th3)
  cv2.waitKey(0)
  cv2.destroyAllWindows()