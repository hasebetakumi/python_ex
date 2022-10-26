import matplotlib.pyplot as plt

import ex6_8
import ex6_6

imglist = ex6_6.create_imglist()
imglist_xy_mean = ex6_8.create_imglist()

# 平均値をとったイメージリストを元々のピクセル数(240x160)に拡張
imglist_xy_mean_240160 = []
for row in imglist_xy_mean:
    xlist = []
    for x in row:
        for _ in range(8):
            xlist.append(x)
    for _ in range(8):
        imglist_xy_mean_240160.append(xlist)

# imglistの指定範囲をimglist_xy_mean_240160で置き換える
new_imglist = []
for y_index, row in enumerate(imglist):
    xlist = []
    for x_index, x in enumerate(row):
        if (50 <= x_index <= 98) and (36 <= y_index <= 100):
            xlist.append(imglist_xy_mean_240160[y_index][x_index])
        else:
            xlist.append(imglist[y_index][x_index])
    new_imglist.append(xlist)

plt.imshow(new_imglist, cmap='gray')
plt.show()
