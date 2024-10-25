with open('input.txt') as f:
    a2 = f.read().splitlines()
a, b = list(map(int, a2[0].split()))
c = str(a2[1])
d1 = int(a2[2])
a = int(str(a), d1)
b = int(str(b), d1)
if c == '+':
    d = a + b
if c == '-':
    d = a - b
if c == '*':
    d = a * b
s = ''
while d > 0:
    s = str(d % d1) + s
    d //= d1
with open('output.txt', 'w') as f:
    f.write(s)