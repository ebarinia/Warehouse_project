DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE suppliers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  location VARCHAR(255),
  active BOOLEAN
);

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description TEXT,
  quantity INT,
  buying_cost FLOAT,
  selling_price FLOAT,
  supplier_id INT NOT NULL REFERENCES suppliers(id),
  category_id INT NOT NULL REFERENCES categories(id)
);