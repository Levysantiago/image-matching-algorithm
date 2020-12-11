import cv2
from helpers import *
import lr2Matching as lr2m
import SIFT as sift

path = "./assets/"
testsPath = "./tests/"
srcImages = [
    ('mundi.jpg', 'mundi2.jpg'),
    ('cube.jpg', 'cube2.jpg'),
    ('many.jpg', 'many2.jpg'),
    ]

for i in srcImages:
    # Abrindo imagens
    A, width, height = loadImage(path+i[0])
    B, width, height = loadImage(path+i[1])

    # Abrindo imagens para SIFT
    A_SIFT = cv2.imread(path+i[0])
    B_SIFT = cv2.imread(path+i[1])

    # Executando algoritmo com grayvalues
    image = lr2m.lr2Matching(A, B)
    lr2m.saveImage(testsPath+"LR2M_"+i[0], image)

    # Executando algoritmo com RGB
    image = lr2m.lr2MatchingRGB(A, B)
    lr2m.saveImage(testsPath+"LR2M_RGB_"+i[0], image)

    # Executando SIFT
    image = sift.SIFT(A_SIFT, B_SIFT)
    sift.saveImage(testsPath+"SIFT_"+i[0], image)