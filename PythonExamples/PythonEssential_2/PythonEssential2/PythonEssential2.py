class Base:
    def method(self):
        print('Hello')

class Child(Base):
    def child_method(self):
        print("From child method")
    def method(self):
        print("Hello from child method")

obj = Child()
obj.method() 
obj.child_method()
