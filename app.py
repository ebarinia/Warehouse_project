from flask import Flask, render_template

from controllers.item_controller import items_blueprint
from controllers.inventory_controller import inventory_blueprint
from controllers.supplier_controller import suppliers_blueprint

app = Flask(__name__)

app.register_blueprint(items_blueprint)
app.register_blueprint(inventory_blueprint)
app.register_blueprint(suppliers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/new')
def new_page():
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)