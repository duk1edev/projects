from example9 import Person
import pickle

john = Person('John', 15)
alex = Person('alex', 23)

Person.make_siblings(john, alex)

print(john, alex)

with open('data/example9.pkl', 'wb') as data:
    pickle.dump((john, alex), data)
