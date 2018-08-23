import numpy as np
import cv2
import contrast

img = cv2.imread('images/with_diabetes/3esim.png')
img = cv2.resize(img, (720, 576))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = contrast.apply(gray, 16)
cv2.imshow('th1', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

# np.savetxt('text2.txt',gray,fmt='%.2f')
