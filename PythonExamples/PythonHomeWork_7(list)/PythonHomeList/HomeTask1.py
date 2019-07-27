def min_max(my_list):
    print("min = {}".format(min(my_list)))
    print("max = {}".format(max(my_list)))

my_list = []

size = int(input("Enter the size of list: "))

for x in range(0,size,1):
     my_list.append(input("index[{}] = ".format(x)))

print("My_List: {}",format(my_list))  

min_max(my_list)


