# map, filter, zip, and reduce
from functools import reduce
my_data = [1, 2, 3]
your_data = [10, 20, 30, 40, 50]
their_list = (5, 4, 3)


def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


# map
print(f'Initial Data: {my_data}')
print(f'Map Function: {list(map(multiply_by2, my_data))}')

# filter
print(f'Filter Function: {list(filter(only_odd, my_data))}')

# zip
print(f'Zip Function: {list(zip(your_data, my_data, their_list))}')

# reduce


def accumulator(acc, item):
    return acc + item


print(f'Reduce Function: {reduce(accumulator,my_data,0)}')
