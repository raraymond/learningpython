class PlayerCharacter:
    # class object attribute
    membership = True

    def __init__(self, name="anonymous", age=0):
        if(age > 18):
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Ryan', 34)
player2 = PlayerCharacter('Ashley', 34)
player2.attack = 50

print(player1.shout())

# print(player1)
# print(player2.attack)

# print(player1.run())
# print(player1.name)
# print(player1.age)
