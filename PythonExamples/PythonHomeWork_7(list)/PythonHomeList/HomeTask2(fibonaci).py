def search_method(step):
     #if step == 0 or step == 1:
     #    return 1
     #else:
     #    return (search_method(step - 1) + search_method(step - 2))
     """Search method
     The as fibonaci list
     """
     step_list = [1,1]
     for i in range(step - 2):
         step_list.append(step_list[i] + step_list[i + 1])
     return step_list


step = int(input("Enter the N - steps to find methods: > "))
N = search_method(step)
print(N)
print("To get to the {0} step , you need to can make {1} methods".format(step,N[len(N)-1]))
