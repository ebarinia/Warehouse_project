DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE suppliers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  location VARCHAR(255),
  active BOOLEAN
);

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description TEXT,
  quantity INT,
  buying_cost FLOAT,
  selling_price FLOAT,
  supplier_id INT NOT NULL REFERENCES suppliers(id)
);