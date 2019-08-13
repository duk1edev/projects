class  Reverse(object):
    def __init__(self,numbers):
        self.numbers=numbers
        self.index = len(numbers) - 1

    def __iter__(self):
        return self
    
    def __next__(self):

        if self.index < 0:
            raise StopIteration

        value = self.numbers[self.index]
        self.index -= 1
        return value

if __name__ == '__main__':
    my_list = [1,2,3,4,5,6]

    for number in Reverse(my_list):
        print(number)
    
