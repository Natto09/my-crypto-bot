from flask import Flask, render_template
import threading, time
import os

app = Flask(__name__)

bot_data = {"status": "Running", "balance": "1,000 USDT"}

@app.route('/')
def index():
    return render_template('index.html', data=bot_data)

if __name__ == '__main__':
    # บรรทัดนี้สำคัญ: Railway จะส่งค่า PORT มาให้ ถ้าไม่มีจะใช้ 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
