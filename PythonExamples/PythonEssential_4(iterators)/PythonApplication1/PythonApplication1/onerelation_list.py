class List:
    class _Node:
        __slots__ = ('value','next')

        def __init__(self,value,next=None):
            self.value = value
            self.next = next

    def __init__(self,iterable=None):
        self._head = None
        self._tail = None
        self._length = 0
    
    if iterable is not None:
            self.extend(self,iterable)
    
    def append(self,value):
        node = List._Node(value)

        if len(self) == 0:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node 
        self._length += 1
    
    def __len__(self):
        return self._length

    def extend(self,iterable):
        for value in iterable:
            self.append(value)

    def __getitem__(self,index):
        if index < 0:
            index += len(self)
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')
        
        node = self._head
        for _ in range(index):
            node = node.next

        return node.value