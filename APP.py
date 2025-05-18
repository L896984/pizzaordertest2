from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Rbg7766734',
    'database': 'pizza_order'
}

# 價格設定（後端計算用）
pizza_prices = {
    'margherita': 200,
    'pepperoni': 250,
    'hawaiian': 230
}

size_prices = {
    'small': 0,
    'medium': 50,
    'large': 100
}

topping_price = 30  # 每項加料價格

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    pizza_type = request.form.get('pizzaType')
    pizza_size = request.form.get('pizzaSize')
    toppings = request.form.getlist('topping')  # 可能多選
    # 後端計算總價
    total_price = pizza_prices.get(pizza_type, 0) + size_prices.get(pizza_size, 0) + topping_price * len(toppings)
    
    toppings_str = ','.join(toppings)  # 字串存資料庫

    # 連線資料庫寫入訂單
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO orders (pizza_type, pizza_size, toppings, total_price) VALUES (%s, %s, %s, %s)"
    vals = (pizza_type, pizza_size, toppings_str, total_price)
    cursor.execute(sql, vals)
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/')  # 下單成功回首頁

if __name__ == '__main__':
    app.run(debug=True)
