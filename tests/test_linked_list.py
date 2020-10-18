import pytest

from linked_list.linked_list import LinkedList


def test_linked_list_length():
    """Verify list if list returns its length properly."""

    linked_list_empty = LinkedList()
    assert linked_list_empty.length == 0

    input_list = [1, 2, 3, 4]
    linked_list_not_empty = LinkedList(input_list)
    assert len(linked_list_not_empty) == len(input_list)

    linked_list_not_empty.append(5)
    expected_list_size = 5
    assert len(linked_list_not_empty) == expected_list_size


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

    input_list = [1, 2, 3, 4, 5]
    linked_list = LinkedList(input_list)

    min_index = 0
    max_index = len(input_list) - 1
    under_min_index = min_index - 1
    over_max_index = len(input_list)

    assert linked_list[min_index] == input_list[0]
    assert linked_list[max_index] == input_list[-1]

    with pytest.raises(IndexError):
        linked_list[under_min_index]

    with pytest.raises(IndexError):
        linked_list[over_max_index]


def test_linked_list_set_index():
    init_list = [1, 2, 3]
    linked_list = LinkedList(init_list)

    min_index = 0
    max_index = len(init_list) - 1
    under_min_index = min_index - 1
    over_max_index = max_index + 1

    min_index_new_value = 1000
    max_index_new_value = 2000

    linked_list[min_index] = min_index_new_value
    linked_list[max_index] = max_index_new_value

    assert linked_list[min_index] == min_index_new_value
    assert linked_list[max_index] == max_index_new_value

    with pytest.raises(IndexError):
        linked_list[under_min_index] == 0

    with pytest.raises(IndexError):
        linked_list[over_max_index] == 0
