from db.run_sql import run_sql
from models.supplier import Supplier

def save(supplier):
    sql = "INSERT INTO suppliers (name, location, active) VALUES (%s, %s, %s) RETURNING id"
    values = [supplier.name, supplier.location, supplier.active]

    results = run_sql( sql, values )
    supplier.id = results[0]['id']
    return supplier

def update(supplier):
    sql = "UPDATE suppliers SET (name, location, active) = (%s, %s, %s) WHERE id = %s"
    values = [supplier.name, supplier.location, supplier.active, supplier.id]
    run_sql(sql, values)

def select_all():
    suppliers = []
    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)
    for row in results:
        supplier = Supplier(row['name'],row['location'], row['active'], row['id'])
        suppliers.append(supplier)
    return suppliers

def select(id):
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        supplier = Supplier(result['name'], result['location'], result['active'], result['id'])
    return supplier

def delete_all():
    sql = "DELETE  FROM suppliers"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

