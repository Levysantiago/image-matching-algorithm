import cv2
from helpers import *
import lr2Matching as lr2m
import SIFT as sift
import time as t
import plotGraph as plot

path = "./assets/"
testsPath = "./tests/"
srcImages = [
    ('mundi.jpg', 'mundi2.jpg'),
    ('cube.jpg', 'cube2.jpg'),
    ('many.jpg', 'many2.jpg'),
    ('apple.jpg', 'apple2.jpg'),
    ('appleCima.jpg', 'appleCima2.jpg'),
    ]

values = []
testCount = 0
lr2m_times = []
lr2mRGB_times = []
SIFT_times = []

for i in srcImages:
    # Abrindo imagens
    A, width, height = loadImage(path+i[0])
    B, width, height = loadImage(path+i[1])

    # Abrindo imagens para SIFT
    A_SIFT = cv2.imread(path+i[0])
    B_SIFT = cv2.imread(path+i[1])

    # Executando algoritmo com grayvalues
    start = t.time()
    image = lr2m.lr2Matching(A, B)
    end = t.time()
    lr2m.saveImage(testsPath+"LR2M_"+i[0], image)

    # Calculando tempo em milisegundos
    lr2m_times.append(round((end-start)*1000, 2))

    # Executando algoritmo com RGB
    start = t.time()
    image = lr2m.lr2MatchingRGB(A, B)
    end = t.time()
    lr2m.saveImage(testsPath+"LR2M_RGB_"+i[0], image)

    # Calculando tempo em milisegundos
    lr2mRGB_times.append(round((end-start)*1000, 2))

    # Executando SIFT
    start = t.time()
    image = sift.SIFT(A_SIFT, B_SIFT)
    end = t.time()
    sift.saveImage(testsPath+"SIFT_"+i[0], image)

    # Calculando tempo em milisegundos
    SIFT_times.append(round((end-start)*1000, 2))

    # Definindo valores para gráfico
    testCount += 1
    values.append("T"+str(testCount))

# print(values)
# print(lr2m_times)
# print(lr2mRGB_times)
# print(SIFT_times)

plot.plot_graph(lr2m_times, lr2mRGB_times, SIFT_times, len(lr2m_times))