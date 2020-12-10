from lr2Matching import *

# Abrindo imagens
A, width, height = loadImage('./assets/apple.jpg')
B, widthB, heightB = loadImage('./assets/apple2.jpg')

# Executando algoritmo
lr2Matching(A, B)