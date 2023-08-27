import pdb
from models.supplier import Supplier
from models.item import Item

import repositories.item_repository as item_repository
import repositories.supplier_repository as supplier_repository

supplier_repository.delete_all()
item_repository.delete_all()

supplier_1 = Supplier('iFixit', 'Edinburgh', True)
supplier_repository.save(supplier_1)

supplier_2 = Supplier('Ikea', 'Glasgow', True)
supplier_repository.save(supplier_2)

supplier_3 = Supplier('Randall & Sons', 'Dunfermline', True)
supplier_repository.save(supplier_3)

item_1 = Item('screwdriver', 'just a screwdriver', 10, 5.00, 10.00, supplier_1, False)
item_repository.save(item_1)

item_2 = Item('toilet paper', 'simple rolls of toilet paper', 50, 3.00, 6.00, supplier_3, False)
item_repository.save(item_2)

id_test = supplier_repository.select(supplier_2)
print(id_test)

pdb.set_trace()