from PIL import Image, ImageOps

def loadImage(path):
    image = Image.open(path, 'r')
    return image, image.width, image.height

def grayvalues(image):
    return ImageOps.grayscale(image).getdata()

def selectPixels(grayvaluesA, grayvaluesB, width, height, limit):
    selectedPixels = []
    counter = 0
    initialB = None
    for i in range(width):
        for j in range(height):
            if(grayvaluesA[counter] < limit):
                selectedPixels.append([(i,j), counter])
            if(not initialB and grayvaluesB[counter] < limit):
                initialB = [(i,j), counter]
            counter += 1
    initialA = selectedPixels[0]
    return selectedPixels, initialA, initialB, 

def selectPixelsBy(mapA, ipA, ipB, width):
    mapB = [ipB]
    for p in mapA:
        if(p != ipA):
            i = ipB[0][0] + abs(ipA[0][0] - p[0][0])
            j = ipB[0][1] + abs(ipA[0][1] - p[0][1])
            # Invertido, pois os pixels da imagem são organizados de maneira invertida
            goTo = [(j,i), ipB[1] + abs(ipA[1] - p[1])]
            if(i < width and j < width):
                mapB.append(goTo)
    return mapB

def highlightPixels(A, B, mapA, mapB, gvA, gvB, limit, showImage):
    colorIt = []
    for i in range(len(mapB)):
        if(abs(gvA[mapA[i][1]] - gvB[mapB[i][1]]) < limit):
            colorIt.append(mapB[i])
            B.putpixel(mapB[i][0], 0)
    if(showImage):
        B.show()