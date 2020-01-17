from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Generates list of random products"""
    products = []
    for i in range(30):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        product = Product(name=name, price=price, weight=weight, flammability=flammability)
        products.append(product)
    return products


def inventory_report(products):
    """Generates report given a product list"""
    names = []
    price_sum = 0
    weight_sum = 0
    flammability_sum = 0
    for product in products:
        if product.name not in names:
            names.append(product.name)
        price_sum += product.price
        weight_sum += product.weight
        flammability_sum += product.flammability
    print(f'{len(names)} unique names.')
    print(f'Average price:{price_sum/len(products)}')
    print(f'Average weight:{weight_sum / len(products)}')
    print(f'Average flammability:{flammability_sum / len(products)}')


if __name__ == '__main__':
    inventory_report(generate_products())
