def print_hello(name="Vitalii"):
    print("Hello , {}!".format(name))

def main():
    name = input("Enter your name: ")
    if name == '':
        print_hello()
    else:
        print_hello(name)

main()