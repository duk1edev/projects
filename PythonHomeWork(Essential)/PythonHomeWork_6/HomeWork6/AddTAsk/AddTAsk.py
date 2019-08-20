def my_dict_func(**dict):
    for key in dict:
        print('key = ',key,'  value = ',dict[key])

dictionary  = {'one':1,'two':2,'three':3,'four':4}

my_dict_func(**dictionary)
my_dict_func(five=5,six=6)