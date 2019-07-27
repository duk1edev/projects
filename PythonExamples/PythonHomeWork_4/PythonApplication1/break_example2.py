name = None

while True:
    print("""Menu:
    1. Enter name 
    2. Print gritting
    3. Quit
    """)
    response  = input("Please choose an action: ")

    print()

    if response == "1":
        name = input("Enter your name: ")
    elif response == "2":
        if name:
            print("Hello {}!".format(name))
        else:
            print("I dont know your name")
    elif response == "3":
        break
    else:
        print("Incorrect input")

    print()