import numpy as np
import cv2
import contrast
import divider

img = cv2.imread('images/with_diabetes/3esim.png')
cv2.imshow('img', img)
cv2.waitKey(0)
img = cv2.resize(img, (720, 576))
# img = cv2.resize(img, (45, 36))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# gray = contrast.apply(gray, 16)
imgs, img = divider.apply(gray)
cv2.imshow('img', img)
for i in range(0, len(imgs)):
  cv2.imshow('img'+str(i), imgs[i])

cv2.waitKey(0)
cv2.destroyAllWindows()

# np.savetxt('text2.txt',gray,fmt='%.2f')
