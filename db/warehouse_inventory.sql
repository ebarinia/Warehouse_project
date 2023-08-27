DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS suppliers;
-- DROP TABLE IF EXISTS inventory;

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description TEXT,
  quantity INT,
  buying_cost FLOAT,
  selling_price FLOAT,
--   supplier_id NOT NULL REFERENCES suppliers(id),
  sold_out BOOLEAN
);

CREATE TABLE suppliers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  location VARCHAR(255),
  active BOOLEAN
);

-- CREATE TABLE inventory (
--   id SERIAL PRIMARY KEY,
--   item_id NOT NULL REFERENCES items(id)
-- );

