from linked_list.linked_list import LinkedList


def test_linked_list_length():
    """Verify list if list returns its length properly."""

    linked_list_ins = LinkedList()

    assert linked_list_ins.length == 0

    element_ins1 = 2
    element_ins2 = 3
    element_ins3 = 4
    linked_list_ins.append(element_ins1)
    linked_list_ins.append(element_ins2)
    linked_list_ins.append(element_ins3)

    assert linked_list_ins.length == 3


def test_linked_list_refs():
    """Verify if references pointers to previous and next element works."""

    linked_list_ins = LinkedList()

    first_element = "First"
    second_element = "Second"

    linked_list_ins.append(first_element)
    linked_list_ins.append(second_element)

    assert linked_list_ins.first_element.data == first_element
    assert linked_list_ins.last_element.data == second_element
    assert linked_list_ins.first_element.prev_pointer is None
    assert linked_list_ins.first_element.next_pointer.data == second_element
    assert linked_list_ins.last_element.prev_pointer.data == first_element
    assert linked_list_ins.last_element.next_pointer is None


def test_lined_list_iterator():
    """Verify iterating mechanism."""

    linked_list_ins = LinkedList()

    first, second, third = 1, 2, 3

    linked_list_ins.append(first)
    linked_list_ins.append(second)
    linked_list_ins.append(third)

    assert [1, 2, 3] == [data for data in linked_list_ins]


def test_linked_list_init():
    """Verify LinkedList initialization."""

    collection = [0, 1, 2, 3]
    linked_list = LinkedList(collection)

    assert [0, 1, 2, 3] == [data for data in linked_list]


def test_linked_list_get_index():
    linked_list = LinkedList([1, 2, 3, 4, 5])

    assert linked_list[2] == 3


def test_linked_list_set_index():
    linked_list = LinkedList([1, 2, 3])
    linked_list[2] = 1000

    assert linked_list[0] == 1
    assert linked_list[1] == 2
    assert linked_list[2] == 1000
