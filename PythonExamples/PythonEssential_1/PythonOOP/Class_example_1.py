class MyObject:
    
    int_field = 5
    str_field = "a string"

print(MyObject.int_field)
print(MyObject.str_field)

object1 = MyObject()
object2 = MyObject()

print(object1.int_field)
print(object2.str_field)

MyObject.int_field = 10
print(MyObject.int_field)
print(object1.int_field)

object1.int_field = 999
print(MyObject.int_field)
print(object1.int_field)   

print(id(MyObject))
print(id(object1))
print(id(object2))


