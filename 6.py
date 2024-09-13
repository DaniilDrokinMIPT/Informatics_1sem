def dd(n, c):
    s = ''
    while n > 0:
        s += str(n % c)
        n //= c
    return int(s[::-1])


f = open('input-7').readlines()
a, b = list(map(int, f[0].split()))
c = f[1]
d = int(f[2])
a1 = int(str(a), d)
b1 = int(str(b), d)
if c == '+':
    c1 = a1 + b1
elif c == '-':
    c1 = a1 - b1
else:
    c1 = a1 * b1
j = open('output-7', 'w')
j.write(str(dd(c1, d)))
j.close()