x = float(input("x = "))

if 0 < x < 7:
    print("Value is in range, lets continue...")
    y = 2 * x - 5
    if y < 0:
        print("y is negative")
    elif y > 0:
            print("y is positive")
    else:
            print("y equals 0")
else:
    print("Value is out of range")
