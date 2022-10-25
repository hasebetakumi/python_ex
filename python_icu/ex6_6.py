import csv
import matplotlib.pyplot as plt
import numpy as np


def create_imglist():
    imglist = []

    with open('Week6_Data/240x160data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            # numpy配列にしてfloat
            float_row = np.float_(row)
            # listに戻す
            list_row = list(float_row)
            imglist.append(list_row)

    return imglist


if __name__ == '__main__':
    imglist = create_imglist()
    plt.imshow(imglist, cmap='gray')
    plt.show()
