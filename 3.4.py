n = int(input())
symb = input()
for i in range(n // 2 + 2):
    print(symb * i)
for i in range(n // 2):
    print((n // 2 - i) * symb)