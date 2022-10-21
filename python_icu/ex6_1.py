import matplotlib.pyplot as plt

imglist = []

for y in range(100):
    xlist = []
    for x in range(100):
        xlist.append(y * x % 50)
    imglist.append(xlist)

plt.imshow(imglist, cmap='gray')
plt.show()
