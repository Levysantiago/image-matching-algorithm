from PIL import Image, ImageOps

def loadImage(path):
    image = Image.open(path, 'r')
    return image, image.width, image.height

def grayvalues(image):
    return ImageOps.grayscale(image).getdata()

def pixels(image):
    return image.getdata()

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
    return selectedPixels, initialA, initialB

def selectPixelsRGB(pixelsA, pixelsB, width, height, limit):
    selectedPixels = []
    counter = 0
    initialB = None
    for i in range(width):
        for j in range(height):
            mean = (pixelsA[counter][0] + pixelsA[counter][1] + pixelsA[counter][2] / 3)
            if(mean < limit):
                selectedPixels.append([(i,j), counter])
            meanB = (pixelsB[counter][0] + pixelsB[counter][1] + pixelsB[counter][2] / 3)
            if(not initialB and meanB < limit):
                initialB = [(i,j), counter]
            counter += 1
    initialA = selectedPixels[0]
    return selectedPixels, initialA, initialB

def selectPixelsBy(mapA, ipA, ipB, width):
    mapB = [ipB]
    for p in mapA:
        if(p != ipA):
            i = ipB[0][0] + (p[0][0] - ipA[0][0])
            j = ipB[0][1] + (p[0][1] - ipA[0][1])
            # Invertido, pois os pixels da imagem são organizados de maneira invertida
            goTo = [(j,i), ipB[1] + abs(ipA[1] - p[1])]
            if(i < width and j < width):
                mapB.append(goTo)
    return mapB

def highlightPixels(A, B, mapA, mapB, gvA, gvB, limit):
    colorIt = []
    C = Image.open(B.filename)
    size = len(mapB)
    for i in range(size):
        if(abs(gvA[mapA[i][1]] - gvB[mapB[i][1]]) < limit):
            colorIt.append(mapB[i])
            C.putpixel(mapB[i][0], 255)
    return C

def highlightPixelsRGB(A, B, mapA, mapB, pixelsA, pixelsB, limit):
    colorIt = []
    # C = Image.new('RGB', (200,200))
    C = Image.open(B.filename)
    size = len(mapB)
    for i in range(size):
        # print(selectedPixels2[i])
        mean = (pixelsA[mapA[i][1]][0] + pixelsA[mapA[i][1]][1] +pixelsA[mapA[i][1]][2] / 3)
        mean2 = (pixelsB[mapB[i][1]][0] + pixelsB[mapB[i][1]][1] +pixelsB[mapB[i][1]][2] / 3)
        if(abs(mean - mean2) < limit ):
            colorIt.append(mapB[i])
            C.putpixel((mapB[i][0]), 255)
    return C