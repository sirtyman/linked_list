# How to use

## Create an empty list:

```
>> linked_list = LinkedList()
>> linked_list.append(1)
```

## Create a list from collection

```>> linked_list = LinkedList([1, 2, 3, 4])```

## Getting element at position idx:

```
>> linked_list = LinkedList([1, 2, 3, 4])
>> linked_list[2]
3
```

## Iterating over the list
```
>> linked_list = LinkedList([1, 2, 3, 4])
>> objs = [obj for obj in linked_list]
>> objs 
[1, 2, 3, 4]
```

# Issues

- The insert() method is not implemented.
- Equality is not implemented.
