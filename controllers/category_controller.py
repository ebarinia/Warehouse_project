from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.category import Category

import repositories.item_repository as item_repository
import repositories.supplier_repository as supplier_repository
import repositories.category_repository as category_repository

category_blueprint = Blueprint("inventory", __name__)