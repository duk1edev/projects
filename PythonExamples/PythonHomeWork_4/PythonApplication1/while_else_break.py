attempts_left = 3
while attempts_left > 0:
    attempts_left -= 1
    password = input("Enter the password ( have left {} attempts) : ".format(attempts_left + 1))
    if password == "qwerty":
        print("Access granted")
        break
else:
    print("Access denied!")

