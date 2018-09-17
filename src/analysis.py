import numpy
import cv2

colors = {}
predominant = None
image = None

def add_predominant(pixel):
  global predominant
  count = colors[str(pixel)]

  if (predominant != None and predominant['pixel'] == pixel):
    predominant['count'] = count
    return

  if (predominant == None or predominant['count'] < count ):
    predominant = {
      'pixel': pixel,
      'count': count
    }

def add_color(pixel):
  global colors
  count = colors[str(pixel)] if str(pixel) in colors else 0
  colors[str(pixel)] = count + 1

def process(i, j):
  pixel = image[i][j]
  add_color(pixel)
  add_predominant(pixel)

def apply(img):
  global image
  image = img
  print(len(img))
  print(len(img[0]))
  soma = 0
  for i in range(0, len(img)):
    for j in range(0, len(img[i])):
      process(i, j)
      soma += 1

  print(soma)
  print(colors)
  print('*' * 50)
  print(predominant)