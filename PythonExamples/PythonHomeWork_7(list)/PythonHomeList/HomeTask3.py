#create simple number
N = int(input("Enter the lenth of number list: "))

simple_number = []

for i in range(2,N+1):
    flag = True
    for j in range(2,i):
        if i % j == 0:
            flag = False
            break
    if flag:
            simple_number.append(i)
print(simple_number)