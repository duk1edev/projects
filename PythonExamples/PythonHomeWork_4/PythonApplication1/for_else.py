for attempts in range(3,0,-1):
    password = input("Enter the password ( have left {} attempts) : ".format(attempts))
    if password == "qwerty":
        print("Access granted")
        break
else:
    print("Access denied!")