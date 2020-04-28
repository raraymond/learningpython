class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} arrows remaining')

    def run(self):
        print(f'{self.name} ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('AX9283', 1000, 10000)

print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
