import numpy as np
import cv2
from matplotlib import patches, pyplot, pyplot as plt
import random
import PIL

small_image_size = 256
big_image_size = 512

def CreateBig():
    big_arr = np.random.randint(0, high=255, size=(big_image_size, big_image_size))
    cv2.imwrite("big.png", big_arr)

def CreateSmall():
    small_arr = np.random.randint(0, high=255, size=(small_image_size, small_image_size))
    cv2.imwrite("small.png", small_arr)

def create():
    positionY = 128
    positionX = 124
    small = cv2.imread("small.png", 0)
    bigR = cv2.imread("big.png", 0)
    bigL = cv2.imread("big.png", 0)

    bigL[positionX:positionX + small_image_size, positionY:positionY + small_image_size] = small
    bigR[positionX:positionX + small_image_size, positionY - 8:positionY + small_image_size - 8] = small

    cv2.imwrite("left.png", bigL)
    cv2.imwrite("right.png", bigR)

def main():
    CreateBig()
    CreateSmall()
    create()
main()