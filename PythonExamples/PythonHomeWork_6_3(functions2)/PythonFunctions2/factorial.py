def nonrecirsive_factorial(n):
    result = 1
    for m in range(2,n + 1):
        result *= m
    return result


def recursion_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursion_factorial(n - 1)

print(recursion_factorial(1000 )) 
