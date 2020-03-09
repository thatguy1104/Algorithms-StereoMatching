import numpy as np
import cv2
from matplotlib import pyplot as plt
import random

def Draw(image1, image2):
    fig = plt.figure()

    a = fig.add_subplot(1, 2, 1)
    imgplot1 = plt.imshow(image1, cmap='gray')
    imgplot1.axes.get_xaxis().set_visible(False)
    imgplot1.axes.get_yaxis().set_visible(False)
    a.set_title('Original Random Dot')


    a = fig.add_subplot(1, 2, 2)
    imgplot2 = plt.imshow(image2, cmap='gray')
    imgplot2.axes.get_xaxis().set_visible(False)
    imgplot2.axes.get_yaxis().set_visible(False)
    a.set_title('Shifted Random Dot')

    plt.show()

def main():
    height = 512
    image1 = np.zeros((height, height))
    image2 = np.zeros((height, height))
    for i in range(0, height - 1):
        for j in range(0, height - 1):
            randomint = random.randrange(0, 254, 1)
            image1[i][j] = randomint
            image2[i][j] = randomint

    Draw(image1, image2)

main()