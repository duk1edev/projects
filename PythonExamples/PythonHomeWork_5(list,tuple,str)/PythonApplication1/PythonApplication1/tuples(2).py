def mean(first, *numbers):
    sum_ = first + sum(numbers)
    return sum_ / (len(numbers)+1)

print('sum = ',mean(1,2,3,4))
