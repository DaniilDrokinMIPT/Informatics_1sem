b = int(input())
a = [1, 2, 5, 10, 50, 100, 500, 1000]
a = a[::-1]
summ = dict()
cash = b
i = 0
while cash > 0:
    if cash >= a[i]:
        cash -= a[i]
        if a[i] in summ.keys():
            summ[a[i]] += 1
        else:
            summ[a[i]] = 1
    else:
        i += 1
for key, val in summ.items():
    if val != 0:
        print(key, val, sep=':')