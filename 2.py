n, s = list(map(str, input().split()))
n = int(n)
s1 = ''
i = 0
for x in range(len(s) // n):
    s1 += s[i:i+n][::-1]
    i += n
print(s1)