from flask import Flask, render_template, request, jsonify
from db_config import get_connection
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_order', methods=['POST'])
def submit_order():
    data = request.get_json()
    phone = data.get('phone')
    items = data.get('items')  # [{'name': 'Pizza A', 'price': 290}, ...]

    if not phone or not items:
        return jsonify({'error': '資料不完整'}), 400

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # 計算總金額
        total_price = sum(item['price'] for item in items)

        # 新增一筆訂單
        cursor.execute(
            "INSERT INTO orders (customer_name, total_price) VALUES (%s, %s)",
            (phone, total_price)
        )
        order_id = cursor.lastrowid

        # 將每筆品項寫入 order_items
        for item in items:
            cursor.execute(
                "INSERT INTO order_items (order_id, item_id, quantity) VALUES (%s, %s, %s)",
                (order_id, get_item_id_by_name(cursor, item['name']), 1)
            )

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'success': True, 'order_id': order_id})

    except Exception as e:
        print("錯誤：", e)
        return jsonify({'error': '內部錯誤'}), 500

# 根據名稱找出 menu_items 的 id
def get_item_id_by_name(cursor, name):
    # 移除「（加起司）」註記以找對應菜單
    base_name = name.split("（")[0]
    cursor.execute("SELECT id FROM menu_items WHERE name = %s", (base_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        # 沒有在資料庫中對應的品項（可以選擇先插入或給 None）
        return None

if __name__ == '__main__':
    app.run(debug=True)
