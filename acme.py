from random import randint


class Product:
    """Creates a named product with some characteristics"""
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        ratio = self.price/self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif 0.5 <= ratio < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        check = self.flammability * self.weight
        if check < 10:
            return "...fizzle."
        elif 10 <= check < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """Creates a boxing glove product subclass."""
    def __init__(self, name, weight=10):
        super().__init__(name)
        self.weight = weight
    
    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
