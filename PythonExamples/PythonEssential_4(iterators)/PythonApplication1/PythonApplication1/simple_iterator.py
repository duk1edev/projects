class SimpleItarator:
    def __getitem__(self,index):
        if 0 <= index <= 5:
            return index * 2
        else:
            raise IndexError


iterable = SimpleItarator()
for value in iterable:
    print(value)