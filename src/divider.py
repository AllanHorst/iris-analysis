import numpy
import cv2

def range_list(list_size, my_range):
  my_list = list(range(list_size))
  my_range = int(list_size / my_range)
  return [my_list[i:i+my_range] for i in range(0, len(my_list), my_range)]

def apply(img):
  size = 6

  heigth = img.shape[0]
  width = img.shape[1]

  cols = range_list(heigth, size)
  rows = range_list(width, size)
  imgs = []
  for i in range(0, size):
    print([cols[i][0], cols[i][len(cols[i]) -1]])
    print([rows[i][0], rows[i][len(cols[i]) -1]])
    piece = img[cols[i][0]:cols[i][len(cols[i]) -1], rows[i][0]:rows[i][len(cols[i]) -1]]
    imgs.append(piece)

    img[cols[i][0]:cols[i][len(cols[i]) -1], rows[i][0]:rows[i][len(cols[i]) -1]] = 0

  return imgs, img