from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.supplier import Supplier

import repositories.item_repository as item_repository
import repositories.supplier_repository as supplier_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

@suppliers_blueprint.route("/suppliers/")
def list_suppliers():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", all_suppliers = suppliers)

@suppliers_blueprint.route("/suppliers/new_supplier")
def new_supplier():
    supplier = supplier_repository.select_all()
    return render_template('new/new_supplier.html', supplier = supplier)

@suppliers_blueprint.route("/suppliers", methods=['POST'])
def add_supplier():
    name         = request.form['name']
    location     = request.form['location']
    active       = request.form['active']
    supplier     = Supplier(name, location, active)
    supplier_repository.save(supplier)
    return redirect('suppliers')

@suppliers_blueprint.route("/suppliers/<id>")
def show_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template('suppliers/show.html', supplier = supplier)

@suppliers_blueprint.route("/suppliers/<id>/edit")
def edit_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template('suppliers/edit.html', supplier = supplier)

@suppliers_blueprint.route("/suppliers/<id>", methods=['POST'])
def update_supplier(id):
    name         = request.form['name']
    location     = request.form['location']
    active       = request.form['active']
    supplier     = Supplier(name, location, active, id)
    supplier_repository.update(supplier)
    return redirect('/suppliers')

@suppliers_blueprint.route("/suppliers/<id>/delete", methods=['POST'])
def delete(id):
    supplier_repository.delete(id)
    return redirect('/suppliers')