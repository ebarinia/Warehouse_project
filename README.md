
![item-explorer](https://github.com/ebarinia/Warehouse_project/assets/46579070/e7f8da02-13b8-4f6e-9263-b09e4fb59ab6)[Youtube Demo](https://youtu.be/vSLNiOuU1V8)

### Brief

The client has several warehouses across Scotland, and has asked me develop an app to help her manage her stock. Using Python, Flask and SQL, create a full-stack application that would keep track of the inventory, as well as a list of suppliers. For each product, the inventory manager should provide valuable information as well as where it was purchased from.

### MVP

- A user should be able to track individual products, including a name, description, stock quantity, additional expense, buying cost, sold status and selling price.

- A user should be able to track the supplier, including its name, location and whether this supplier is still working with them.

- A user you should be able to create and edit an item and a supplier separately.

- The inventory and list of suppliers should be sorted in some ways, either by type, name, or quantity

- The inventory should show an inventory page, listing all the details and quantity for all the products in stock in a single view.

- The inventory should display whether an item has sold out or has low stock, as well as showing stock quantity as a number.

### ⭐ Extensions ⭐
 
- Calculate the markup for an item, and display it on the item page next to the quantity

- Filter the inventory list by name. For example, being to display all the item starting with the same name

- Categorise your items. Books might be categorised by genre (crime, horror, romance...) and cars might be categorised by type (SUV, coupé, hatchback...). Provide an option to filter the inventory list by these categories.

## Setup & Installation

#### 1. Git clone the repo on local machine

```
#terminal
git clone git@github.com:ebarinia/Warehouse_project.git
```

#### 2. Create the database
- Check wether PostgreSQL/PSYCOPG2 are installed on the machine
```
#terminal
psql
```
- If not installed, find the installation guide [here](https://www.psycopg.org/docs/install.html)
- Create database
```
#terminal
createdb warehouse_inventory
```
- initializing the tables for the database
```
#terminal
psql -d warehouse_inventory -f db/warehouse_inventory.sql
```

#### 3. Initialize the database

- populate the database with dummy data
```
#terminal (cd in the root folder)
python3 console.py
```

#### 4. Starting the app

- make sure that nothing else is running on your localhost port 4999. If so, change the port on the .flaskenv file to a different one (like 5000)
- start the app
```
#terminal
flask run
```

