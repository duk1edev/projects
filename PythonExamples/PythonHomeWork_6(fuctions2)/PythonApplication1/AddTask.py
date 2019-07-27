def sum_all_numbers(start,end):
    if end == start :
        return end
    else:
        sum =  start + sum_all_numbers(start+1,end)
    return sum

start = int(input("Start: "))
end = int(input("End: "))
result = sum_all_numbers(start,end)
print("From {} to {} sum of all numbers = {}".format(start,end,result))

