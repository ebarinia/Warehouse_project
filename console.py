import pdb

import repositories.item_repository as item_repository
import repositories.supplier_repository as supplier_repository

from models.supplier import Supplier
from models.item import Item


item_1 = Item('screwdriver', 'just a screwdriver', 10, 5.00, 10.00, False)
item_repository.save(item_1)

item_2 = Item('toilet paper', 'simple rolls of toilet paper', 50, 3.00, 6.00, False)
item_repository.save(item_2)

supplier_1 = Supplier('iFixit', 'Edinburgh', True)
supplier_repository.save(supplier_1)

pdb.set_trace()