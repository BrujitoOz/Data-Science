from PIL import ImageChops
import numpy as np
import pywt

def is_greyscale(im):
    if im.mode == "RGB":
        rgb = im.split()
        if ImageChops.difference(rgb[0],rgb[1]).getextrema()[1]!=0: 
            return False
        if ImageChops.difference(rgb[0],rgb[2]).getextrema()[1]!=0: 
            return False
    return True
def transform(image):
    coeffs2 = pywt.dwt2(image, 'haar')
    LL, (LH, HL, HH) = coeffs2
    return [LL, LH, HL, HH]
def reconstruct(coeffs):
    coeffs2 = coeffs[0], (coeffs[1], coeffs[2], coeffs[3])
    return pywt.idwt2(coeffs2, 'haar')
def mergeChannelsToImg(redChannel,greenChannel,blueChannel):
    width = redChannel[0].size
    height = redChannel.size//width
    channels = 3
    img = np.zeros((height, width, channels), dtype=np.uint8)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            r, g, b = (redChannel[y][x],greenChannel[y][x],blueChannel[y][x])
            img[y][x][0] = boundValue(r)
            img[y][x][1] = boundValue(g)
            img[y][x][2] = boundValue(b)
    return img
def boundValue(value):
    if(value>254):
        return 255
    elif (value < 0):
        return 0
    else:
        return value