from db.run_sql import run_sql

from models.inventory import Inventory
from models.item import Item
from models.supplier import Supplier

def save(item):
    sql = "INSERT INTO items (name, description, quantity, buying_cost, selling_price, sold_out) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [item.name, item.description, item.quantity, item.buying_cost, item.selling_price, item.sold_out]

    results = run_sql( sql, values )
    item.id = results[0]['id']
    return item

def select_all():
    items = []
    sql = "SELECT * FROM items"
    results = run_sql(sql)
    for row in results:
        item = Item(row['name'],row['description'], row['quantity'], row['buying_cost'], row['selling_price'], row['sold_out'], row['id'])
        items.append(item)
    return items