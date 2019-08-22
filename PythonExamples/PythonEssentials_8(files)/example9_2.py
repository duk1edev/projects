import pickle
import example9

with open('data/example9.pkl', 'rb') as tata:
    people = pickle.load(tata)

print(people)