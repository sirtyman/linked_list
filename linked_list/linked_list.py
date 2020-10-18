class Element:
    def __init__(self, data, index):
        self.data = data
        self.index = index
        self.prev_pointer = None
        self.next_pointer = None


class LinkedList:
    def __init__(self, collection=[]):
        self.collection = collection

        self.first_element = None
        self.last_element = None
        self.length = 0

        self.next = self.__next__

        self._initialize()

    def _initialize(self):
        for obj in self.collection:
            self.append(obj)

    @staticmethod
    def _find_index(index, element):
        if element.index == index:
            ret_element = element
        elif element.next_pointer is None:
            raise IndexError("Cannot find element at index {}".format(index))
        else:
            ret_element = LinkedList._find_index(index, element.next_pointer)

        return ret_element

    def append(self, obj):
        self.length += 1
        element = Element(obj, self.length - 1)

        if not self.first_element:
            self.first_element = element
            self.last_element = element
            return
        else:
            self.last_element.next_pointer = element
            element.prev_pointer = self.last_element
            self.last_element = element

    def insert(self, index, value):
        raise NotImplementedError("This method is not yet implemented!")

    def __iter__(self):
        self._iter_el = self.first_element
        return self

    def __next__(self):
        if self._iter_el is None:
            raise StopIteration
        else:
            current = self._iter_el
            self._iter_el = self._iter_el.next_pointer

        return current.data

    def __getitem__(self, index):
        if index < 0:
            raise IndexError('Index of LinkedList shall be 0 or any positive value.')
        elif index > len(self):
            raise IndexError('Index out of bounds')

        element = LinkedList._find_index(index, self.first_element)
        return element.data

    def __setitem__(self, index, value):
        if index < 0:
            raise IndexError('Index of LinkedList shall be 0 or any positive value.')
        elif index > len(self):
            raise IndexError('Index out of bounds')

        element = LinkedList._find_index(index, self.first_element)
        element.data = value

    def __len__(self):
        return self.length


