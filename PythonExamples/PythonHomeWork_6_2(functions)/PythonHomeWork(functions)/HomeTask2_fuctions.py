def calculate_expression1(a):
    return  a ** 3
def calculate_expression2(a):
    return 2 + a

def print_table_expression(calculate_exp):
    i = -5
    #if calculate_exp == calculate_expression1:
    while i < 5:
        result_def = calculate_exp(i)
        print("{1} = funtion({0})".format(result_def,i))
        i += 0.5
            
def main():
    print_table_expression(calculate_expression1)
    print()
    print_table_expression(calculate_expression2)

main()