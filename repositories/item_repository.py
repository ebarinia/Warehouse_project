from db.run_sql import run_sql
from models.item import Item
import pdb

import repositories.supplier_repository as supplier_repository

def save(item):
    sql = "INSERT INTO items (name, description, quantity, buying_cost, selling_price, supplier_id, sold_out) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [item.name, item.description, item.quantity, item.buying_cost, item.selling_price, item.supplier.id, item.sold_out]

    results = run_sql( sql, values )
    item.id = results[0]['id']
    return item

def update(item):
    # pdb.set_trace()
    sql = "UPDATE items SET (name, description, quantity, buying_cost, selling_price, supplier_id, sold_out) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s RETURNING *"
    values = [item.name, item.description, item.quantity, item.buying_cost, item.selling_price, item.supplier.id, False, item.id]
    result = run_sql(sql, values)
    # pdb.set_trace()

def select_all():
    items = []
    sql = "SELECT * FROM items"
    results = run_sql(sql)
    for row in results:
        supplier = supplier_repository.select(row['supplier_id'])
        item = Item(row['name'],row['description'], row['quantity'], row['buying_cost'], row['selling_price'], supplier , row['sold_out'], row['id'])
        items.append(item)
    return items

def select(id):
    item = None
    sql = "SELECT * FROM items WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        supplier = supplier_repository.select(result['supplier_id'])
        item = Item(result['name'], result['description'], result['quantity'], result['buying_cost'], result['selling_price'], supplier, result['sold_out'], result['id'])
    return item

def delete_all():
    sql = "DELETE  FROM items"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM items WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def item_from_supplier(supplier):
    items = []
    sql = "SELECT * FROM items WHERE supplier_id = %s"
    values = [supplier.id]
    results = run_sql(sql, values)

    for row in results:
        item = Item(row['name'], row['description'], row['quantity'], row['buying_cost'], row['selling_price'], supplier, row['sold_out'], row['id'])
        items.append(item)
    return items