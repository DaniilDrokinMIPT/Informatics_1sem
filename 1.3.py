a = list(map(float, input().split()))
i = 1
for x in a:
    i *= x
print(pow(i, 1 / len(a)))