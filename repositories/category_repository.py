from db.run_sql import run_sql

from models.category import Category
from models.item import Item
from models.supplier import Supplier

def save(category):
    sql = "INSERT INTO categories (name) VALUES (%s) RETURNING id"
    values = [category.name]

    results = run_sql( sql, values )
    category.id = results[0]['id']
    return category

def select_all():
    categories = []
    sql = "SELECT * FROM categories"
    results = run_sql(sql)
    for row in results:
        category = Category(row['name'], row['id'])
        categories.append(category)
    return categories

def select(id):
    category = None
    sql = "SELECT * FROM categories WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        category = Category(result['name'], result['id'])
    return category

def delete_all():
    sql = "DELETE  FROM categories"
    run_sql(sql)

def items_by_category(category):
    items = []
    sql = "SELECT * FROM items WHERE category_id = %s"
    values = [category.id]
    results = run_sql(sql, values)

    for row in results:
        supplier = supplier_repository.select(row['supplier_id'])
        item = Item(row['name'], row['description'], row['quantity'], row['buying_cost'], row['selling_price'], supplier, category, row['id'])
        items.append(item)
    return items