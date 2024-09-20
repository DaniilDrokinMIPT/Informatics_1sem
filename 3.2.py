def ra(n):
    ch = []
    i = 2
    while n > 1:
        if n % i == 0:
            ch.append(i)
            n //= i
        else:
            i += 1
    return ch


print(*ra(int(input())))