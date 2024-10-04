ogr = int(input())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
e = []
for i in range(len(a)):
    e.append((-c[i] / a[i], a[i], c[i]))
e.sort()
weight = 0
cost = 0
i = 0
while weight + e[i][1] <= ogr:
    weight += e[i][1]
    cost += e[i][2]
    i += 1
print(cost)