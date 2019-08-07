class ObjectWithDestructor:
    def __del__(self):
        print('Destructor ivoked')
        raise Exception

print('Creating object...')
obj = ObjectWithDestructor()

print('Deleting reference...')
del obj

print('Done')