import numpy as np
import cv2
import contrast
import analysis
import pupil_finder
import normalize

img = cv2.imread('images/with_diabetes/4dsim.png', 0)
imgs = pupil_finder.find(img)
if (not imgs or len(imgs) != 4):
  print('Pupil not founded')
else:
  normalize.four_pieces(imgs)
  cv2.imshow('detected circles', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()