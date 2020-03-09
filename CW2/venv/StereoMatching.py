import numpy as np
import cv2
from matplotlib import pyplot as plt


def calculate_STEREO(ImageRight, ImageLeft):
    num_of_rows = ImageRight.shape[0]
    num_of_columns = ImageLeft.shape[1]
    # Initiate the disparity arrays with 0's
    disparity_left = np.zeros((num_of_rows, num_of_columns))
    disparity_right = np.zeros((num_of_rows, num_of_columns))
    # Set occlusion value (given as 3.8)
    occlusion_value = 12

    for all_rows in range(0, num_of_rows):
        # Inform the user of the process made so far
        print("processing " + str(all_rows) + " / " + str(num_of_rows))
        CostMatrix = np.zeros((num_of_columns, num_of_columns))
        DisparityMatrix = np.zeros((num_of_columns, num_of_columns))

        for i in range(0, num_of_columns):
            CostMatrix[i][0] = i * occlusion_value
            CostMatrix[0][i] = i * occlusion_value

        for i in range(0, num_of_columns):
            for j in range(0, num_of_columns):
                if ImageLeft[all_rows][i] > ImageRight[all_rows][j]:
                    cost_of_match = ImageLeft[all_rows][i] - ImageRight[all_rows][j]
                else:
                    cost_of_match = ImageRight[all_rows][j] - ImageLeft[all_rows][i]

                minimum_one = CostMatrix[i - 1][j - 1] + cost_of_match
                minimum_two = CostMatrix[i - 1][j] + occlusion_value
                minimum_three = CostMatrix[i][j - 1] + occlusion_value
                # Keep the minimum cost in memory
                CostMatrix[i][j] = min(minimum_one, minimum_two, minimum_three)
                c_minimum = min(minimum_one, minimum_two, minimum_three)

                if minimum_one == c_minimum:
                    DisparityMatrix[i][j] = 1
                elif minimum_two == c_minimum:
                    DisparityMatrix[i][j] = 2
                elif minimum_three == c_minimum:
                    DisparityMatrix[i][j] = 3

        i = num_of_columns - 1
        j = num_of_columns - 1

        while i != 0 and j != 0:
            if DisparityMatrix[i][j] == 1:
                disparity_left[all_rows][i] = abs(i - j)
                disparity_right[all_rows][j] = abs(j - i)
                i = i - 1
                j = j - 1
            elif DisparityMatrix[i][j] == 2:
                disparity_left[all_rows][i] = 0
                i = i - 1
            elif DisparityMatrix[i][j] == 3:
                disparity_right[all_rows][j] = 0
                j = j - 1

    depth = (disparity_left * 255) / np.amax(disparity_left)
    plt.subplot(111), plt.imshow(disparity_left, cmap='gray')
    plt.title('Left Disparity'), plt.xticks(), plt.yticks()
    plt.show()


def main():
    leftIMAGE = cv2.imread(
        "/Users/albert.ov11/Desktop/OneDrive - University College London/Algorithms/CW/venv/view1.png", 0)
    leftIMG = np.asarray(leftIMAGE, dtype=np.uint8)
    rightIMAGE = cv2.imread(
        "/Users/albert.ov11/Desktop/OneDrive - University College London/Algorithms/CW/venv/view2.png", 0)
    rightIMG = np.asarray(rightIMAGE, dtype=np.uint8)

    calculate_STEREO(leftIMG, rightIMG)


main()