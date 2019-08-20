def fibonaci_sequence():
    first,second = 0,1

    while True:
        yield second
        first,second = second,first + second
   
def fibonaci(limit):
    generator = fibonaci_sequence()
    for _ in range(limit):
        yield next(generator)

def nth_fibonaci(number):
    result = None
    for current in fibonaci(number):
        result = current
    return result


if __name__ == '__main__':
    print('Running tests')
    assert nth_fibonaci(1) == 1
    assert nth_fibonaci(2) == 1
    assert nth_fibonaci(3) == 2
    assert nth_fibonaci(4) == 3
    assert nth_fibonaci(5) == 5
    print('End testing')
