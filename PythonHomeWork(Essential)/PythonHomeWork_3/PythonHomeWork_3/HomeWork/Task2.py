#calculator
def Addition(a,b):
    """ Add A + B, and return result of addition
    """
    return a + b

def Substraction(a,b):
    """Sub A - B, and return result of substration
    """
    return a - b

def Multiply(a,b):
    """Sub A - B, and return result of multiplication
    """
    return a * b
def Divine(a ,b):
    """Div A - B, and return result of divide
    """
    return a / b
def Pow(a,b):
    """Powering number A in pow B
    """
    return pow(a,b)
print("Calculator")
while True:
    result = 0
        

    try:
        print("Enter the numbers")
        a = float(input('a = '))
        b = float(input('b = '))
    except ValueError as error:
        print("a or b must be  number, please try again")
    else:
        print("""
  Choose the operation
1.+
2.-
3.*
4./
5.** - (pow(a,b))
        """)
        sing = str(input('Operation: ')) 
        
        if sing == '1' or sing == '+':
            result = Addition(a,b)
            print('{} + {} = {}'.format(a,b,result))
            
        elif sing == '2' or sing == '-':
            result = Substraction(a,b)
            print('{} - {} = {}'.format(a,b,result))

        elif sing == '3' or sing == '*':
            result = Multiply(a,b)
            print('{} * {} = {}'.format(a,b,result))
        elif sing == '4' or sing == '/':
            try:
                b == 0
                raise ZeroDivisionError
            except ZeroDivisionError as error:
                print("You could't divine by zero")
            else:
                result = Divine(a,b)
                print('{} / {} = {}'.format(a,b,result))
        elif sing == '**' or sing == 'pow' or sing == '5':
            try:
                 if  a == 0 and b < 0:
                    raise ZeroDivisionError
            except ZeroDivisionError:
                     print("You coud'nt increse zero in minus frequency")
            else:
                result = Pow(a,b)
                print('{} / {} = {}'.format(a,b,result))
    print()



