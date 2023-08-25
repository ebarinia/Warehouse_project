class Item():

    def __init__(self, name, description, quantity, buying_cost, selling_price, supplier, sold = False, low_quantity = False, id = None):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.supplier = supplier
        self.sold = sold
        self.low_quantity = low_quantity
        self.id = id