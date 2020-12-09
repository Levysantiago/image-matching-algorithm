def calculatePixelsDiferences(pixels, size):
    mean = 0
    finalList = []
    for p in pixels:
        _sum = abs(abs(p[0]) - abs(p[1]) - p[2])
        mean += _sum
        finalList.append([p, _sum])
    mean = mean/size
    return finalList, mean

def calculatePixelsSimilarities(a,b, sizeA, sizeB, mean, difference):
    size = sizeB
    if(sizeA < sizeB):
        size = sizeA

    similarity = 0
    for i in range(0, size):
        if(a[i][0][0] < mean):
            left = abs(a[i][0][0] -  b[i][0][0])
            middle = abs(a[i][0][1] -  b[i][0][1])
            right = abs(a[i][0][2] -  b[i][0][2])
            if(left+middle+right < difference):
                # print(a[i])
                # print(b[i])
                # print(a[i][1] -  b[i][1])
                similarity += 1
    return similarity