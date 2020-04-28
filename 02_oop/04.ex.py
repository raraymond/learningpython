# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def adding_things(num1, num2):
        return num1 + num2


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Wolverine', 7)
cat2 = Cat('Minnie', 2)
cat3 = Cat('Sabertooth', 4)

# 2 Create a function that finds the oldest cat


def oldest_cat(*cats):
    return max(cats)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(
    f"the oldest cat is {oldest_cat(cat1.age, cat1.age, cat3.age)} years old.")
