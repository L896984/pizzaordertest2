from flask import Flask, request, redirect, render_template
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', ''),
        database=os.environ.get('DB_NAME', 'pizza_order')
    )

pizza_prices = {'margherita': 200, 'pepperoni': 250, 'hawaiian': 230}
size_prices = {'small': 0, 'medium': 50, 'large': 100}
topping_price = 30

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    pizza_type = request.form.get('pizzaType')
    pizza_size = request.form.get('pizzaSize')
    toppings = request.form.getlist('topping')

    total_price = pizza_prices.get(pizza_type, 0) + size_prices.get(pizza_size, 0) + topping_price * len(toppings)
    toppings_str = ','.join(toppings)

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO orders (pizza_type, pizza_size, toppings, total_price) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (pizza_type, pizza_size, toppings_str, total_price))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
