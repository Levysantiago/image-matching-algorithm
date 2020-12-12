from helpers import *

def lr2Matching(A, B):
    width = A.width
    height = A.height
    gvA = grayvalues(A)
    gvB = grayvalues(B)
    mapA, ipA, ipB = selectPixels(gvA, gvB, width, height, 160)
    mapB = selectPixelsBy(mapA, ipA, ipB, width)
    return highlightPixels(A, B, mapA, mapB, gvA, gvB, 160)

def lr2MatchingRGB(A, B):
    width = A.width
    height = A.height
    pixelsA = pixels(A)
    pixelsB = pixels(B)
    mapA, ipA, ipB = selectPixelsRGB(pixelsA, pixelsB, width, height, 300)
    mapB = selectPixelsBy(mapA, ipA, ipB, width)
    return highlightPixelsRGB(A, B, mapA, mapB, pixelsA, pixelsB, 150)

def showImage(image):
    image.show()

def saveImage(path, image):
    image.save(path)