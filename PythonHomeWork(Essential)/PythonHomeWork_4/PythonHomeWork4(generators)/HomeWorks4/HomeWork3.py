"""
Пример реализации списка с итератором
"""


class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам
        # последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)

    def clear(self):
        node = self._head

        while node is not None:
            next_node = node.next
            del node
            node = next_node

        self._head = self._tail = None
        self._length = 0

    def insert(self,index,value):

        if index < 0:
            index += len(self)

        if index < 0:
            index = 0
        if index > len(self):
            index = len(self)

        if index == len(self):
            self.append(value)
        else:
            node = MyList._ListNode(value)

            place = self._get_node_by_index(index)

            left = place.prev

            if left is not None:
                left.next = node
            else:
                self._head = node

            place.prev = node
            node.prev = left
            node.next = place

            self.__length +=1

    def _get_node_by_index(self,index):
        if index < 0:
            index += len(self)

        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1 
        node = self._get_node_by_index(index)

        value = node.value

        left = node.prev
        rigth = node.next

        if left is not None:
            left.next = rigth
        else:
            self._head = rigth

        if rigth is not None:
            rigth.prev = left
        else:
            self._tail = left

        del node
        self._length -=1

        return value

def main():
    # Создание списка
    my_list = MyList([1, 2, 5])

    # Вывод длины списка
    print(len(my_list))

    # Вывод самого списка
    print(my_list)

    print()

    # Обход списка
    for element in my_list:
        print(element)

    print()

    # Повторный обход списка
    for element in my_list:
        print(element)

    print()

    print('Print insert')
    my_list.insert(8,999)
    my_list.insert(8,998)
    my_list.insert(8,997)
    my_list.insert(8,996)
    for x in my_list:
        print(x)

    print('Show after pop element by index 5')
    
    my_list.pop(5)
    for x in my_list:
        print(x)

    my_list.clear()
    print('my_list after func CLEAR')
    for element in my_list:
        print(element)

    

if __name__ == '__main__':
    main()
