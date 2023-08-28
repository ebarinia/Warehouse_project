from flask import Flask, render_template, request, redirect
from flask import Blueprint
import pdb

import repositories.item_repository as item_repository
import repositories.supplier_repository as supplier_repository

items_blueprint = Blueprint("items", __name__)

@items_blueprint.route("/items")
def list_items():
    items = item_repository.select_all()
    # pdb.set_trace()
    return render_template("items/index.html", all_items = items)

@items_blueprint.route("/items/<id>")
def show_item(id):
    item = item_repository.select(id)
    return render_template('items/show.html', item = item)

# @items_blueprint.route("/items/<id>", methods=['POST'])
# def delete_item(id):
#     item_repository.delete(id)
#     return redirect('/items') -----> This is for the delete button - if I decide to do one