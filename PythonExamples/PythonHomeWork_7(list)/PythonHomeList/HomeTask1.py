def min_max(my_list):
    """Searchin min and max value of list
    """
    print("Min = ",min(my_list,key = abs))
    print("Max = ",max(my_list,key = abs))

def sum_all_element(my_list):
    """Get the all elements of list 
    and return sum of all elements of list
    """
    result = 0
    for i in range(len(my_list)):
        result = result + int(my_list[i])
    return result

def middle_arif(my_list):
    """Находит среднее ариметичское значение 
    их всех сначений списка
    """
    result = sum_all_element(my_list) / len(my_list)
    return result

my_list = []

size = int(input("Enter the size of list: "))

for x in range(size):
     my_list.append(int(input("index[{}] = ".format(x))))

print("My_List: {}",format(my_list))  

min_max(my_list)
print("Sum of all list elements : {}".format(sum_all_element(my_list)))
print("Middle arif : {}".format(middle_arif(my_list)))