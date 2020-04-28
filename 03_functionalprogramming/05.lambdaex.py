my_list = [5, 4, 3]
# make a one line lambda that prints a square of the list
print(f'{my_list} squared: {list(map(lambda item: item**2, my_list))}')

# list sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(f'sorted by second element {a}')
