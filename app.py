from flask import Flask, render_template
import threading, time

app = Flask(__name__)

bot_data = {"status": "Running", "balance": "1,000 USDT"}

@app.route('/')
def index():
    return render_template('index.html', data=bot_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)