from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.item_repository as item_repository
import repositories.supplier_repository as supplier_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

@suppliers_blueprint.route("/suppliers")
def suppliers():
    list_suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", all_suppliers = list_suppliers)
