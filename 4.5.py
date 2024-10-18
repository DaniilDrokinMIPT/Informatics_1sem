import matplotlib.pyplot as plt
import csv
import datetime
import numpy as np


def data(a):
    a = a[:10]
    data2 = datetime.date(int(a[0:4]), int(a[5:7]), int(a[8:10]))
    return data2.strftime('%d-%m-%Y')

c = []
y = []
with open('BTC_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        a = row['time']
        b = row['close']
        c.append(data(a))
        y.append(float(b))
print(c, y)
plt.plot(c, y, 'b-')
plt.xticks(['01-06-2018', '03-06-2019', '01-06-2020', '02-06-2021',
            '01-06-2022', '01-06-2023'])
plt.show()

