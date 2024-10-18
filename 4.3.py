import matplotlib.pyplot as plt
import csv


a = []
b = []
with open('iris_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        a.append(row['Species'])
        b.append(row['PetalLengthCm'])
d = dict()
for x in a:
    if x in d.keys():
        d[x] += 1
    else:
        d[x] = 1
s1 = []
for key, val in d.items():
    s1.append(val)
s2 = [0] * 3
for x in b:
    if float(x) < 1.2:
        s2[0] += 1
    elif float(x) <= 1.5:
        s2[1] += 1
    else:
        s2[2] += 1

fig = plt.figure(figsize=(16, 9))
axs1 = fig.add_subplot(211)
axs2 = fig.add_subplot(212)
axs1.pie(s1, labels=[x for x in d.keys()])
axs1.set_title('Виды')


axs2.pie(s2, labels=['<1.2', '1.2 - 1.5', '>1.5'])

axs2.set_title('Длины')

plt.show()
