def ra(n):
    ch = dict()
    i = 2
    while n > 1:
        while n % i == 0:
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
f = f'{n} = '
for key, val in res.items():
    if val != 0:
        f += f'{key}^{val}*'
print(f[:len(f) - 1:])