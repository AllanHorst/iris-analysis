import numpy as np
import cv2
import contrast
import divider
import analysis

img = cv2.imread('images/with_diabetes/4dsim.png')
# img = cv2.resize(img, (720, 576))
img = cv2.resize(img, (360, 288))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = contrast.apply(gray, 16)
imgs, img = divider.apply(gray)
cv2.imshow('img2', gray)
cv2.imshow('img', imgs[5])
# for i in range(0, len(imgs)):
#   cv2.imshow('img'+str(i), imgs[i])

analysis.apply(imgs[5])
np.savetxt('text1.txt',imgs[5],fmt='%.2f')
cv2.waitKey(0)
cv2.destroyAllWindows()
