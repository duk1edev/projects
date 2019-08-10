def fibonacci(n):
    first, second = 0,1
    for _ in range(n):
        yield second
        first, second = second, first + second
        
count  = int(input ('Numbers: '))

for fib in fibonacci(count):
    print(fib)