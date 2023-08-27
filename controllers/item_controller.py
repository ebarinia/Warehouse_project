from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.item_repository as item_repository
import repositories.supplier_repository as supplier_repository

items_blueprint = Blueprint("items", __name__)

@items_blueprint.route("/items")
def items():
    items = item_repository.select_all()
    return render_template("locations/index.html", all_items = items)