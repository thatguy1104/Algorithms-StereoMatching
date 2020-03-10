import numpy as np
import cv2
from matplotlib import patches, pyplot, pyplot as plt
import random
import PIL

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

def Overlay(im1, im2):
    bigA = im1
    smallB = im2
    positionY = 124
    positionX = 128
    bigA[positionX:(positionX+smallB.shape[0]), positionY:(positionY+smallB.shape[0])] = smallB
    # cv2.rectangle(bigA, (positionY, positionX), (positionY + smallB.shape[0], positionX+ smallB.shape[0]), (255, 0, 0), 5)
    return bigA

def OverlayShift(im1, im2):
    bigA = im1
    smallB = im2
    positionY = 132
    positionX = 128
    bigA[positionX:(positionX+smallB.shape[0]), positionY:(positionY+smallB.shape[0])] = smallB
    # cv2.rectangle(bigA, (positionY, positionX), (positionY + smallB.shape[0], positionX+ smallB.shape[0]), (255, 0, 0), 5)
    return bigA

def CreateBig():
    Big1 = 512
    Big_one = np.zeros((Big1, Big1))
    for i in range(0, Big1 - 1):
        for j in range(0, Big1 - 1):
            randomint = random.randrange(0, 255, 1)
            Big_one[i][j] = randomint
    return Big_one

def CreateSmall():
    Small1 = 256
    Small = np.zeros((Small1, Small1))
    for i in range(0, Small1 - 1):
        for j in range(0, Small1 - 1):
            randomint = random.randrange(0, 255, 1)
            Small[i][j] = randomint
    return Small

def main():
    A = CreateBig()
    B = CreateSmall()
    L = Overlay(A, B)
    cv2.imwrite("left.png", L)
    R = OverlayShift(A, B)
    cv2.imwrite("right.png", R)
main()