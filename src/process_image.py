import numpy as np
import cv2
import contrast
import analysis
import pupil_finder
import normalize

def process(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  imgs = pupil_finder.find(img)
  smudges = 0
  if (not imgs or len(imgs) != 4):
    print('Pupil not founded')
  else:
    pieces = normalize.four_pieces(imgs)
    for i in range(0, len(pieces)):
      if (analysis.analyze(pieces[i])):
        smudges += 1

  return smudges == 4

img = cv2.imread('images/without_diabetes/5d.png')
img = cv2.imread('images/with_diabetes/5esim.png')
img = cv2.imread('images/with_diabetes/4dsim.png')
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# img = cv2.imread('images/without_diabetes_with_background/3e.png')
result = process(img)
print('result: ', result)