from db.run_sql import run_sql

from models.inventory import Inventory
from models.item import Item
from models.supplier import Supplier

def save(user):
    sql = "INSERT INTO users( name ) VALUES ( %s ) RETURNING id"
    values = [user.name]
    results = run_sql( sql, values )
    user.id = results[0]['id']
    return user