def even_numbers(generator):
    def decorated_sequence(*args):
        seq = generator(*args)
        return filter(lambda x: x % 2 == 0, seq)

    return decorated_sequence

@even_numbers
def fibonaci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield b


print(list(fibonaci(10)))