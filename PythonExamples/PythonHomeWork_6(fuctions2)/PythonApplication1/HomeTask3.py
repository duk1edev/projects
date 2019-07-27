def search_method(step):
     if step == 0 or step == 1:
         return 1
     else:
         return (search_method(step - 1) + search_method(step - 2))



step = int(input("Enter the N - steps to find methods: > "))
N = search_method(step)
print("To get to the {0} step , ypu need to can make {1} methods".format(step,N))