def middle(*numbers):
    #my_numbers = numbers[0]
    #
    #sum_ = 0
    #
    #for number in my_numbers:
    #    sum_ += number
    #return sum_ / len(my_numbers)

    return sum(numbers)/len(numbers)


if __name__ == "__main__":
    
    #numbers = (1,23,4,234,123)
    #range_numbers = range(0,10,1)
    #
    #print(middle(numbers))
    #print(middle(range_numbers))

    print(middle(1,23,4,234,123))
    print(middle(*range(0,10,1)))
