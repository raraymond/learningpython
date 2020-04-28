import random as r


print(r.random())
print(r.randint(1, 10))
print(r.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))
my_list = [1, 2, 3, 4, 5]
r.shuffle(my_list)
print(my_list)
