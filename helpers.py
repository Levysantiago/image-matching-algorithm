from PIL import Image, ImageOps

def loadImageAsPixels(path):
    image = Image.open(path, 'r')
    pixels = image.getdata()
    graypixels = (ImageOps.grayscale(image).getdata())

    # ImageOps.grayscale(image).show()
    return pixels, graypixels, image, image.width, image.height