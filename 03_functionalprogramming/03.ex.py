from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

my_pets_capitalized = [pet.capitalize() for pet in my_pets]
print(my_pets_capitalized)

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_numbers, my_strings.sort())))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def filter_pass(score):
    return score > 50


print(f'Filter Function: {list(filter(filter_pass, scores))}')

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def accumulator(acc, item):
    return acc + item


print(
    f'Reduce Function: {reduce(accumulator,my_numbers,reduce(accumulator,scores,0))}')


# from functools import reduce

# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']

# def capitalize(string):
#     return string.upper()

# print(list(map(capitalize, my_pets)))


# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]

# print(list(zip(my_strings, sorted(my_numbers))))


# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]

# def is_smart_student(score):
#     return score > 50

# print(list(filter(is_smart_student, scores)))


# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
# def accumulator(acc, item):
#     return acc + item

# print(reduce(accumulator, (my_numbers + scores)))
