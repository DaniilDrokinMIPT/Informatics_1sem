a = list(map(int, input().split()))
p = -1
t = 0
for x in a:
    if a.count(x) > p:
        p = a.count(x)
        t = x
print(t)