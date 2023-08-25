from flask import Flask, render_template, request, redirect
from flask import Blueprint

inventory_blueprint = Blueprint("inventory", __name__)