from lr2Matching import *

# Abrindo imagens
A, width, height = loadImage('./assets/apple2.jpg')
B, widthB, heightB = loadImage('./assets/apple3.jpg')

# Executando algoritmo
lr2Matching(A, B)