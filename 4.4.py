import matplotlib.pyplot as plt
import csv


a = []
b = []
with open('iris_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        a.append(row['Species'])
        b.append(row['PetalLengthCm'])

fig = plt.figure(figsize=(16, 9))
axs1 = fig.add_subplot(211)
axs2 = fig.add_subplot(212)
axs1.pie(s1, labels=[x for x in d.keys()])
axs1.set_title('Виды')


axs2.pie(s2, labels=['<1.2', '1.2 - 1.5', '>1.5'])

axs2.set_title('Длины')

plt.show()
