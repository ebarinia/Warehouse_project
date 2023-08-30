import pdb
from models.supplier import Supplier
from models.item import Item
from models.category import Category


import repositories.item_repository as item_repository
import repositories.supplier_repository as supplier_repository
import repositories.category_repository as category_repository

supplier_repository.delete_all()
item_repository.delete_all()
category_repository.delete_all()

supplier_1 = Supplier('iFixit', 'Edinburgh', True)
supplier_repository.save(supplier_1)
supplier_2 = Supplier('Ikea', 'Glasgow', True)
supplier_repository.save(supplier_2)
supplier_3 = Supplier('Randall & Sons', 'Dunfermline', True)
supplier_repository.save(supplier_3)

category_1 = Category('Electronics')
category_repository.save(category_1)
category_2 = Category('Tools')
category_repository.save(category_2)
category_3 = Category('Homeware')
category_repository.save(category_3)
category_4 = Category('Clothing')
category_repository.save(category_4)
category_5 = Category('Furniture')
category_repository.save(category_5)

item_1 = Item('screwdriver', 'just a screwdriver', 10, 5.00, 10.00, supplier_1, category_2)
item_repository.save(item_1)
item_2 = Item('toilet paper', 'simple rolls of toilet paper', 50, 3.00, 6.00, supplier_3, category_3)
item_repository.save(item_2)
item_3 = Item('laptop', 'macbook 13 2017', 5, 300.00, 500.00, supplier_1, category_1)
item_repository.save(item_3)
item_4 = Item('iphone 11', 'iphone 11 pro max 256gb', 3, 100.00, 180.00, supplier_1, category_1)
item_repository.save(item_4)

items = item_repository.select_all()
print(items)

pdb.set_trace()