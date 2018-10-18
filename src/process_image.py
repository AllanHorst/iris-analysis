import numpy as np
import cv2
import contrast
import analysis
import pupil_finder
import normalize

def process(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # img = cv2.resize(img,  (300, 300))
  imgs = pupil_finder.find(img)
  if (not imgs or len(imgs) != 4):
    print('Pupil not founded')
  else:
    pieces = normalize.four_pieces(imgs)
    for i in range(0, len(pieces)):
      result = analysis.analyze(pieces[i])
      print(result)

img = cv2.imread('images/without_diabetes/5d.png')
img = cv2.imread('images/with_diabetes/5esim.png')
# img = cv2.imread('images/with_diabetes/4dsim.png')
# img = cv2.imread('images/without_diabetes_with_background/3e.png')
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
result = process(img)
print('result: ', result)