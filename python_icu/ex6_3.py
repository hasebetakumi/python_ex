import csv
import matplotlib.pyplot as plt


def create_templist():
    templist = []

    all_temp = []
    with open('data/TokyoTemp1941-2020.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            all_temp.append(row[1])
        del all_temp[0:3]
        
    year_temp = []
    for temp in all_temp:
        year_temp.append(float(temp))
        if len(year_temp) == 12:
            templist.append(year_temp)
            year_temp = []
    
    return templist


if __name__ == '__main__':
    templist = create_templist()
    plt.imshow(templist, cmap='coolwarm')
    plt.show()
