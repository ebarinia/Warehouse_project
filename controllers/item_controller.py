from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.item import Item

import repositories.item_repository as item_repository
import repositories.supplier_repository as supplier_repository
import repositories.category_repository as category_repository


items_blueprint = Blueprint("items", __name__)

@items_blueprint.route("/items")
def list_items():
    items = item_repository.select_all()
    categories = category_repository.select_all()

    sorted_items = sorted(items, key=lambda items: items.name.lower())
    return render_template("items/index.html", all_items = sorted_items, categories = categories)

@items_blueprint.route("/items/new_item")
def new_item():
    item = item_repository.select_all()
    suppliers = supplier_repository.select_all()
    categories = category_repository.select_all()
    return render_template('new/new_item.html', item = item, suppliers = suppliers, categories = categories)

@items_blueprint.route("/items", methods=['POST'])
def add_item():
    # pdb.set_trace()
    name          = request.form['name']
    description   = request.form['description']
    quantity      = int(request.form['quantity'])
    buying_cost   = float(request.form['buying_cost'])
    selling_price = float(request.form['selling_price'])
    supplier_id   = request.form['supplier']
    category_id   = request.form['category']
    supplier      = supplier_repository.select(supplier_id)
    category      = category_repository.select(category_id)
    item          = Item(name, description, quantity, buying_cost, selling_price, supplier, category)
    item_repository.save(item)
    return redirect('items')

@items_blueprint.route("/items/<id>")
def show_item(id):
    item = item_repository.select(id)
    return render_template('items/show.html', item = item)

@items_blueprint.route("/items/<id>/edit")
def edit_item(id):
    item = item_repository.select(id)
    suppliers = supplier_repository.select_all()
    categories = category_repository.select_all()
    return render_template('items/edit.html', item = item, suppliers = suppliers, categories = categories)

@items_blueprint.route("/items/<id>", methods=['POST'])
def update_item(id):
    # pdb.set_trace()
    name          = request.form['name']
    description   = request.form['description']
    quantity      = int(request.form['quantity'])
    buying_cost   = float(request.form['buying_cost'])
    selling_price = float(request.form['selling_price'])
    supplier_id   = request.form['supplier']
    category_id   = request.form['category']
    supplier      = supplier_repository.select(supplier_id)
    category      = category_repository.select(category_id)
    item          = Item(name, description, quantity, buying_cost, selling_price, supplier, category, id)
    item_repository.update(item)
    return redirect('/items')

@items_blueprint.route("/items/<id>/delete", methods=['POST'])
def delete(id):
    item_repository.delete(id)
    return redirect('/items')