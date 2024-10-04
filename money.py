def change(money, c):
    length = money + 1
    table = [0] * length
    inf = 10 ** 20
    for i in range(1, length):
        table[i] = inf
    table[0] = 0
    for m in range(1, length):
        for i in c:
            if i <= m:
                table[m] = min(table[m], 1 + table[m - i])
    return table[money]


a = int(input())
b = list(map(int, input().split()))
print(change(a, b))