import matplotlib.pyplot as plt
import statistics

import ex6_3


templist = ex6_3.create_templist()

month_temp_ave_list = []
for month in range(12):
    month_temp = []
    for year_temp in templist:
        month_temp.append(year_temp[month])
    month_temp_ave_list.append(statistics.mean(month_temp))

plt.plot(month_temp_ave_list)
plt.legend
plt.show()
