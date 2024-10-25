n, b, c = list(map(int, input().split()))
n = int(str(n), base=b)
s = ''
while n > 0:
    s = str(n % c) + s
    n //= c
print(s)