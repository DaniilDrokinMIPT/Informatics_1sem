n = int(input())
symb = input()
if n % 2 == 0:
    for i in range(n // 2 + 1):
        print(symb * i)
    for i in range(n // 2):
        print(symb * (n // 2 - i))
else:
    for i in range(n // 2 + 2):
        print(symb * i)
    for i in range(n // 2):
        print(symb * (n // 2 - i))