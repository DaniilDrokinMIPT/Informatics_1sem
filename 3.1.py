import sys
from functools import lru_cache

sys.setrecursionlimit(20000)


@lru_cache(None)
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(int(input())))
