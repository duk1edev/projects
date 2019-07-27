#febonacci  = 1 , 1 
import functools

@functools.lru_cache(maxsize=None)

def fib(n):
     if n==1 or n==2:
         return 1
     else:
        return fib(n-1) + fib(n - 2)

for i in range(1,100,1):
     print(fib(i))