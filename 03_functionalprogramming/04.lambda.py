from functools import reduce
my_data = [1, 2, 3]


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


print(f'Map Function With Lambda: {list(map(lambda item: item*2, my_data))}')
print(
    f'Filter Function With Lambda: {list(filter(lambda item: item%2 !=0 , my_data))}')

print(
    f'Reduce Function With Lambda: {reduce(lambda acc, item: acc + item,my_data,0)}')

print(f'Original data: {my_data}')
