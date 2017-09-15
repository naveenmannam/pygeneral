"""
DOG class inheriting from Animal class.
"""

class Animal():
    """
    Animal class
    """

    color = "Black"
    eyes = "Black"
    legs = 4
    has_fur = True

    def make_noise(self):
        print("Animal makes noise")

    def run(self):
        print("Animal moves")


class Dog(Animal):
    name = "Bablu"

    def make_noise(self):
        print(self.name + " is making noise.")

bablu = Dog()

bablu.make_noise()
bablu.run()
print(bablu.name)
