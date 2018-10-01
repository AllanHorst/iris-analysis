import numpy as np
import cv2
import contrast
import analysis
import pupil_finder
import normalize

def process(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  imgs = pupil_finder.find(img)
  if (not imgs or len(imgs) != 4):
    print('Pupil not founded')
  else:
    pieces = normalize.four_pieces(imgs)
    for i in range(0, len(pieces)):
      analysis.analyze(pieces[i])


# img = cv2.imread('images/without_diabetes/3d.png', 0)
# img = cv2.imread('images/with_diabetes/4dsim.png', 0)