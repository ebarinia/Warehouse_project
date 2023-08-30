import math

class Item():

    def __init__(self, name, description, quantity, buying_cost, selling_price, supplier, category, id = None):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.supplier = supplier
        self.category = category
        self.id = id
    
    def calculate_markup(self):
        if self.buying_cost == 0:
            return 0
        markup = math.floor(((self.selling_price - self.buying_cost) / self.buying_cost) * 100)
        return markup