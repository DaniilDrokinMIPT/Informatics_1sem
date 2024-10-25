with open('input.txt') as f:
    a2 = []
    for line in f:
        a2.append(line)
a, b = list(map(int, a2[0].split()))
c = str(a2[1])
if c == '+':
    d = a + b
if c == '-':
    d = a - b
if c == '*':
    d = a * b
with open('output.txt', 'w') as f:
    f.write(str(d))