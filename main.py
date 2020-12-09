from helpers import *
from PIL import ImageOps

A, width, height = loadImage('./assets/apple2.jpg')
B, widthB, heightB = loadImage('./assets/apple3.jpg')

gvA = grayvalues(A)
gvB = grayvalues(B)
mapA, ipA, ipB = selectPixels(gvA, gvB, width, height, 200)
mapB = selectPixelsBy(mapA, ipA, ipB, width)
highlightPixels(A, B, mapA, mapB, gvA, gvB, 250, True)