from flask import Flask, render_template, request, redirect
from flask import Blueprint

items_blueprint = Blueprint("items", __name__)