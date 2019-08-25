def Person(name, age):
    def print_hello():
        print(F'Hello!My name is {name}')

    def get_age():
        return age

    return {'print_hello': print_hello, 'get_age': get_age}


john = Person('John', 25)
john['print_hello']()
print(john['get_age']())
