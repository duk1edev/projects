from functools import lru_cache



@lru_cache(maxsize=None)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n-2)


for i in range(1, 150):
    print(f'{i} = {fib(i)}')