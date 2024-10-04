def ra(n):
    ch = dict()
    i = 2
    while n > 1:
        if n % i == 0:
            if i in ch.keys():
                ch[i] += 1
            else:
                ch[i] = 1
            n //= i
        else:
            i += 1
    return ch


n = int(input())
res = ra(n)
for key, val in res.items():
    if val != 0:
        print(key, val, sep=':')