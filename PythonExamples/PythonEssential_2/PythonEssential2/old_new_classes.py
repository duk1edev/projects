class A:
    pass
class Base(A):
    def method(self):
        print("Method class: ",__class__.__name__)
        print("Instance class: ",type(self).__name__)
        print("")


class Child(Base):
    pass
def main():
    base_instance = Base()
    base_instance.method()
    
    child_instance = Child()
    child_instance.method()

    for cls in [A,Base,Child]:
        print(cls.__name__ + ":",cls.mro())

if __name__ == '__main__':
    main()
