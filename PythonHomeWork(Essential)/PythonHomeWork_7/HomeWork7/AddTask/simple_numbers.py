# Simple numbers module
"""Модуль, для работы с простыми числами"""


def simple_sequence(N):
    """Генератор простых чисел в промежутке от 0 - N"""

    for i in range(2, N + 1):
        for j in range(2, i):
            if i % i == 0:
                break
        else:
            yield i


def show_simple_numbers(length):
    """Показать простые числа в диапазоне от 0 до Length"""

    for number in range(length):
        print(f'{number}')
