import matplotlib.pyplot as plt
import statistics

import ex6_3


templist = ex6_3.create_templist()

year_temp_ave_list = []
for year_temp in templist:
    year_ave = statistics.mean(year_temp)
    year_temp_ave_list.append(year_ave)

plt.plot(year_temp_ave_list)
plt.legend
plt.show()
