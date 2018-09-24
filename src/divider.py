import numpy
import cv2

def range_list(list_size, my_range):
  my_list = list(range(list_size))
  my_range = int(list_size / my_range)
  return [my_list[i:i+my_range] for i in range(0, len(my_list), my_range)]

def apply(img):
  size = 2
  print(size)

  width = img.shape[1]
  heigth = img.shape[0]

  cols = range_list(heigth, size)
  rows = range_list(width, size)
  imgs = []
  for i in range(0, len(cols)):
    list_cols = cols[i]
    col_range = [list_cols[0], list_cols[len(list_cols) -1]]

    for j in range(0, len(rows)):
      list_rows = rows[j]
      row_range = [list_rows[0], list_rows[len(list_rows) -1]]

      piece = img[col_range[0]:col_range[1], row_range[0]:row_range[1]]
      imgs.append(piece)
      cv2.waitKey(0)

      # img[col_range[0]:col_range[1], row_range[0]:row_range[1]] = 0

  return imgs, img