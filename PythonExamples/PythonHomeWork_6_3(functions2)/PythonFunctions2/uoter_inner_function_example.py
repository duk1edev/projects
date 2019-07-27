def outer_function():
    def inner_function():
        print("Inner Fuction")

    print("Outer Function")
    inner_function()

outer_function()