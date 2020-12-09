from helpers import *

def lr2Matching(A, B):
    width = A.width
    height = A.height
    gvA = grayvalues(A)
    gvB = grayvalues(B)
    mapA, ipA, ipB = selectPixels(gvA, gvB, width, height, 200)
    mapB = selectPixelsBy(mapA, ipA, ipB, width)
    highlightPixels(A, B, mapA, mapB, gvA, gvB, 250, True)