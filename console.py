import pdb
from models.item import Item

import repositories.item_repository as item_repository

item_1 = ('screwdriver', 'just a screwdriver', 10, 5.00, 10.00, False)
item_repository.save(item_1)

item_2 = ('toilet paper', 'simple rolls of toilet paper', 50, 3.00, 6.00, False)
item_repository.save(item_2)

pdb.set_trace()