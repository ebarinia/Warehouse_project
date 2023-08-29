class Item():

    def __init__(self, name, description, quantity, buying_cost, selling_price, supplier, id = None):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.supplier = supplier
        self.id = id