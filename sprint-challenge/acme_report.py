
#import needed libraries
from acme import Product
from random import randint, sample, uniform
import itertools

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):

    products = []
    combinations = list(itertools.product(NOUNS, ADJECTIVES))

    for item in list(range(num_products)):
        prod = Product(name=sample(combinations,1),

                       #price random int 5 to 100
                       price=random.randint(5, 100),
                       #weight random int 5 to 100
                       weight=random.randint(5, 100),
                       #flammability random float from 0 to 2.5
                       flam=random.uniform(0, 2.5))

        products.append(prod)
    return products


def inventory_report(products):
    for item in products:
        print(f"Item stats \n Name:{self.name} \n price:{self.price}")
        print(f"weight:{self.weight} \n flammability:{self.flammability}")


if __name__ == '__main__':
    inventory_report(generate_products())
