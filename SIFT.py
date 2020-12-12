import cv2
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TKAgg')

def SIFT(img1, img2, showImage=True, savePath=False):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # sift
    sift = cv2.xfeatures2d.SIFT_create()

    #keypoints
    keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

    matches = bf.match(descriptors_1, descriptors_2)
    matches = sorted(matches, key=lambda x: x.distance)

    img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:50], img2, flags=2)
    return img3

def showImage(image):
        plt.imshow(image), plt.show()

def saveImage(path, image):
    cv2.imwrite(path, image)