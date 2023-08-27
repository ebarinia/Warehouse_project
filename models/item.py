class Item():

    def __init__(self, name, description, quantity, buying_cost, selling_price, sold_out = False, id = None):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        # self.supplier = supplier / Will need to be added back to the class after testing
        self.sold_out = sold_out
        self.id = id