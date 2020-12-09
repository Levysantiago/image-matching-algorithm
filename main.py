from helpers import *
from PIL import ImageOps

pixelsA, gvA, A, width, height = loadImageAsPixels('./assets/apple2.jpg')
pixelsB, gvB, B, widthB, heightB = loadImageAsPixels('./assets/apple3.jpg')

mapA, ipA, ipB = selectPixels(gvA, gvB, width, height, 200)
mapB = selectPixelsBy(mapA, ipA, ipB, width)
highlightPixels(A, B, mapA, mapB, gvA, gvB, 250, True)