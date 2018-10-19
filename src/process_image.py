import numpy as np
import base64
import cv2
import contrast
import analysis
import pupil_finder
import normalize

def process(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # img = cv2.resize(img,  (300, 300))
  imgs = pupil_finder.find(img)
  data = []
  sum_result = 0
  if (not imgs or len(imgs) != 4):
    print('Pupil not founded')
  else:
    pieces = normalize.four_pieces(imgs)
    for i in range(0, len(pieces)):
      result, piece = analysis.analyze(pieces[i])

      retval, buffer = cv2.imencode('.jpg', piece)
      base64_bytes = base64.b64encode(buffer)
      base64_string = base64_bytes.decode('utf-8')
      sum_result += result
      data.append({
        'result': round(result, 2),
        'img': base64_string
      })

  avarage = sum_result / 4
  return { 'images': data, 'avarage': round(avarage, 2) }

# img = cv2.imread('images/without_diabetes/5d.png')
# img = cv2.imread('images/with_diabetes/5esim.png')
# img = cv2.imread('images/with_diabetes/4dsim.png')
# img = cv2.imread('images/without_diabetes_with_background/3e.png')
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# result = process(img)
# print('result: ', result)