import numpy as np
import cv2
import contrast
import analysis
import pupil_finder
import normalize

img = cv2.imread('images/without_diabetes/3d.png', 0)
# img = cv2.imread('images/with_diabetes/4dsim.png', 0)
imgs = pupil_finder.find(img)
if (not imgs or len(imgs) != 4):
  print('Pupil not founded')
else:
  pieces = normalize.four_pieces(imgs)
  print(pieces)
  for i in range(0, len(pieces)):
    analysis.analyze(pieces[i])
