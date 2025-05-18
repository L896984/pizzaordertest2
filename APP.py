from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__, static_folder="static")

# 資料庫連線設定
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Rbg7766734',
    'database': 'pizza_order'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    data = request.json
    pizza_type = data['pizzaType']
    pizza_size = data['pizzaSize']
    toppings = ','.join(data['toppings'])
    total = data['total']

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO orders (pizza_type, pizza_size, toppings, total_price)
            VALUES (%s, %s, %s, %s)
        """, (pizza_type, pizza_size, toppings, total))
        conn.commit()
        return jsonify({'message': '訂單已成功儲存！'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
