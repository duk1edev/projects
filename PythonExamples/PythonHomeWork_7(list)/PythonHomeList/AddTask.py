def rever_list(my_list):
    new_list = my_list[::-1]
    print("Reversed list: {}".format(new_list))

my_list = []

size = int(input("Enter the size of list: "))

for x in range(0,size,1):
     my_list.append(input("index[{}] = ".format(x)))
    

rever_list(my_list)