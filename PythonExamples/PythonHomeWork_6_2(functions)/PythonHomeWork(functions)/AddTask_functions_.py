def count_arif(a, b, c):
    result = (a + b + c) / 3
    return result

def main():
    
    
    while True:
        print("""
             1. Enter the numbers, to count middle.
             2. Exit
             """)
        choise = input("Make your choise: ");
        if choise == "1":
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))
            result = count_arif(a,b,c)
            print("Среднее арифметическое {}, {}, {} = {}".format(a,b,c,result))
        elif choise == "2" or choise == "exit" or choise == "Exit":
            break
        else:
            input("You didnt choose anything!")
    
main()