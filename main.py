from helpers import *
from calculator import *
from PIL import ImageOps

pixels, graypixels, image, width1, height1 = loadImageAsPixels('./assets/apple2.jpg')
pixels2, graypixels2, image2, width2, height2 = loadImageAsPixels('./assets/apple3.jpg')

totalPixels = width1*height1
totalPixels2 = width2*height2

initial = [(0,0), graypixels[0]]
counter = 0
selectedPixels = []
initial2 = None

# Por gray values
for i in range(width1):
    for j in range(height1):
        if(graypixels[counter] < 200):
            selectedPixels.append([(i,j), counter])
        if(not initial2 and graypixels2[counter] < 200):
            initial2 = [(i,j), counter]
        counter += 1

initial = selectedPixels[0]
selectedPixels2 = [initial2]

for p in selectedPixels:
    if(p != initial):
        # goTo = (initial2[0] + abs(initial[0] - p[0]), initial2[1] + abs(initial[1] - p[1]))
        i = initial2[0][0] + abs(initial[0][0] - p[0][0])
        j = initial2[0][1] + abs(initial[0][1] - p[0][1])
        # Invertido, pois os pixels da imagem são organizados de maneira invertida
        goTo = [(j,i), initial2[1] + abs(initial[1] - p[1])]
        if(i < 200 and j < 200):
            selectedPixels2.append(goTo)

# print(initial)
# print(initial2)
# print(selectedPixels[1])
# print(selectedPixels2[1])

colorIt = []

for i in range(len(selectedPixels2)):
    if(abs(graypixels[selectedPixels[i][1]] - graypixels2[selectedPixels2[i][1]]) < 250 ):
        colorIt.append(selectedPixels2[i])
        # print(selectedPixels2[i][0])
        image2.putpixel(selectedPixels2[i][0], 0)

image2.show()


# print(colorIt)