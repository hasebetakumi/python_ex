import matplotlib.pyplot as plt

imglist = []

for y in range(100):
    xlist = []
    for x in range(100):
        if (20 <= y <= 80) and (20 <= x <= 80):
            xlist.append(1)
        else:
            xlist.append(0)
        
    imglist.append(xlist)

plt.imshow(imglist, cmap='gray')
plt.show()
