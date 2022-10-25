import matplotlib.pyplot as plt
import numpy as np

import ex6_6

imglist = ex6_6.create_imglist()


def x_mean_for_8(imglist):
    """
    x軸方向に8個ずつ平均をとる
    """
    imglist_mean_8 = []
    for row in imglist:
        xlist = []
        x_for_8 = []
        for x in row:
            x_for_8.append(x)
            if len(x_for_8) == 8:
                xlist.append(np.mean(x_for_8, axis=0))
                x_for_8 = []
        imglist_mean_8.append(xlist)
    return imglist_mean_8


def create_imglist():
    # x軸方向に8個ずつ平均をとる
    imglist_x_only_mean = x_mean_for_8(imglist)

    #  軸を入れ替える
    imglist_x_only_mean_T = np.transpose(imglist_x_only_mean)

    # 入れ替えたx軸（もともとy軸）に８個ずつ平均をとる
    imglist_yx_mean = x_mean_for_8(imglist_x_only_mean_T)

    # 軸を戻す
    imglist_xy_mean = np.transpose(imglist_yx_mean)

    return imglist_xy_mean


if __name__ == '__main__':
    imglist_xy_mean = create_imglist()
    plt.imshow(imglist_xy_mean, cmap='gray')
    plt.show()
