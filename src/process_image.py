import numpy as np
import cv2
import contrast
import divider
import analysis
import pupil_finder

img = cv2.imread('images/with_diabetes/4dsim.png', 0)
center_x, center_y = pupil_finder.find(img)
cv2.circle(img, (center_x, center_y), 2, (0, 0, 255), 3)

cv2.imshow('detected circles', img)

cv2.waitKey(0)
cv2.destroyAllWindows()