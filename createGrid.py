from PIL import Image
import numpy as np

img = Image.open('bw_wegmans.png').convert('L')

np_img = np.array(img)
np_img[np_img > 0] = 1


def getNewGrid():
    return np_img

