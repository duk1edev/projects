class Base:
    def method(self):
        print("Method from the Base on ",type(self).__name__,'instance')

class Child(Base):
    def method(self):
        super(Child,self).method()
        print("Method from the Child on ",type(self).__name__,'instance')

     
        
