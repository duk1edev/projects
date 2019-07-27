x = float(input("x = "))

if x > 0:
    y = x ** 0.5
else:
    y = x ** 2

print("y = {}".format(y))


name = input("Enter your name : ")

if name == "Vitalii":
    print("You entered {}!".format(name))
    print("Your name the same like mine")
else:
    print("You have different name")
