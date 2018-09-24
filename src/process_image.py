import numpy as np
import cv2
import contrast
import analysis
import pupil_finder
import normalize

img = cv2.imread('images/with_diabetes/4dsim.png', 0)
center = pupil_finder.find(img)
# cv2.circle(img, (center[0], center[1]), center[2], (0, 0, 255), 3)
cv2.circle(img, (center[0], center[1]), 2, (0, 0, 255), 3)
normalize.four_pieces(img, center)
cv2.imshow('detected circles', img)

cv2.waitKey(0)
cv2.destroyAllWindows()