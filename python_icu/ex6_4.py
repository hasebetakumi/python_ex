import matplotlib.pyplot as plt

import ex6_3


templist = ex6_3.create_templist()

plt.plot(templist[0], label=1941)
plt.plot(templist[79], label=2020)
plt.legend
plt.show()
