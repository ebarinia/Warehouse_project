from flask import Flask, render_template, request, redirect
from flask import Blueprint

suppliers_blueprint = Blueprint("suppliers", __name__)