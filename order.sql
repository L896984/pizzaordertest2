CREATE DATABASE IF NOT EXISTS pizza_order;
USE pizza_order;

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pizza_type VARCHAR(50),
    pizza_size VARCHAR(10),
    toppings TEXT,
    total_price INT,
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
