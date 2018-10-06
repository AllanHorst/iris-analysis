import numpy as np
import cv2

def find_smudge(img, y, x):
  smudge = []
  for i2 in range(y, len(img)):
    found = False
    for j2 in range(x, len(img[y])):
      color = img[i2][j2]
      if (color == 255):
        continue

      found = True
      smudge.append([i2, j2])

    if (not found):
      break

  return smudge

def founded(i, j, smudges):
  for k in range(0, len(smudges)):
    for l in range(0, len(smudges[k])):
      if (smudges[k][l][0] == i and smudges[k][l][1] == j):
        return True
  return False

def analyze(img):
  th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY, 61,10)
  blank = np.zeros((img.shape))
  blank.fill(255)
  smudges = []
  black = 0
  white = 0
  for y in range(0, len(img)):
    for x in range(0, len(img[y])):

      if (th3[y][x] == 255):
        continue
      color = img[y][x]
      if (color < 120):
        blank[y][x] = 0

  # for i in range(0, len(smudges)):
  #   smudge = smudges[i]
  #   for j in range(0, len(smudge)):
  #     y = smudge[j][0]
  #     x = smudge[j][1]
  #     color = img[y][x]
  #     if (color < 120):
  #       blank[y][x] = 0

      # blank[y][x] = 0

    # if (smudge)

  # cv2.imshow('img', img)
  cv2.imshow('or', th3)
  cv2.imshow('blank', blank)
  cv2.waitKey(0)
  cv2.destroyAllWindows()