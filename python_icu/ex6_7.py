import matplotlib.pyplot as plt

import ex6_6

imglist = ex6_6.create_imglist()

reverse_imglist = []

for row in imglist:
    xlist = []
    for x in row:
        new_x = 1 - x
        xlist.append(new_x)
    reverse_imglist.append(xlist)

plt.imshow(reverse_imglist, cmap='gray')
plt.show()
