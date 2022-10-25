import numpy as np
import matplotlib.pyplot as plt

import ex6_3


templist = ex6_3.create_templist()

month_temp_ave_list = np.mean(templist, axis=0)

plt.plot(month_temp_ave_list)
plt.legend
plt.show()
