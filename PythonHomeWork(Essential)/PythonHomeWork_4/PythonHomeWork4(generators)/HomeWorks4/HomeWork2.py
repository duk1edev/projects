def my_reversed(numbers):
    _index = len(numbers) - 1
    
    while _index >= 0:
        yield numbers[_index]
        _index -= 1
    
    

if __name__ == '__main__':
    my_list = [1,2,3,4,5,6]

    for number in my_reversed(my_list):
        print(number)
    
