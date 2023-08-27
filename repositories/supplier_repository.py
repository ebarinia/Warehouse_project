from db.run_sql import run_sql

from models.inventory import Inventory
from models.item import Item
from models.supplier import Supplier

def save(supplier):
    sql = "INSERT INTO suppliers (name, location, active) VALUES (%s, %s, %s) RETURNING id"
    values = [supplier.name, supplier.location, supplier.active]

    results = run_sql( sql, values )
    supplier.id = results[0]['id']
    return supplier

def delete_all():
    sql = "DELETE  FROM suppliers"
    run_sql(sql)