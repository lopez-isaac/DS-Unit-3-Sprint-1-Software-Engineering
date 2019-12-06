
"Needed imports"
import random

"""
A class that creates an acme product entry contain infomation about it
"""


class Product:

    """
    create entry for the product and add specifications
    """
    def __init__(self, name="name", price=10, weight=20, flam=.5,
                 id=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flam
        self.identifier = id

    """
    returns a stealability value of the product.
    """
    def stealability(self):
        chance = self.price/self.weight
        if chance < .5:
            return print("Not so stealable")
        if chance >= .5 and chance < 1.0:
            return print("kinda stealable")
        else:
            return print("very stealable")

    """
    returns the explosive level of a product
    """
    def explode(self):
        bomb = self.flammability * self.weight
        if bomb < 10:
            return print('...fizzle')
        if bomb >= 10 and bomb < 50:
            return print("...boom!")
        else:
            return print("...BABOOM!!")

"""
Subclass Boxingglove, parent class Product
"""


class BoxingGlove(Product):

    """
    Create boxing glove entry with info
    """
    def __init__(self, name="name", price=10, weight=20, flam=.5,
                 id=random.randint(1000000, 9999999)):
        super().__init__(weight=10)

    """
    overrrided explode method. returns "its a glove" all the time
    """
    def explode(self):
        bomb = self.flammability * self.weight
        if bomb < 10:
            return print("...it's a glove.")
        if bomb >= 10 and bomb < 50:
            return print("...it's a glove.")
        else:
            return print("...it's a glove.")

    """
    return the level of pain the punch delivered
    """
    def punch(self):
        if self.weight < 5:
            return print("That tickles.")
        if self.weight >= 5 and self.weight < 15:
            return print("Hey that hurt!")
        else:
            return print("OUCH!")
