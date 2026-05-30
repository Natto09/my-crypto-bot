import os
import threading
from flask import Flask

app = Flask(__name__)

# สมมติว่านี่คือฟังก์ชันบอทของคุณ
def run_bot():
    # โค้ดบอทเทรดของคุณอยู่ที่นี่
    print("Bot is running...")

@app.route('/')
def home():
    return "Bot is alive!"

@app.route('/status')
def status():
    # สมมติว่าคุณมีตัวแปรเก็บสถานะการเทรดในบอท
    return f"Bot Status: Running. Last Trade: ..."
 
if __name__ == '__main__':
    # 1. สั่งให้บอทเริ่มทำงานในเบื้องหลัง (Background Thread)
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # 2. ให้ Flask รันเป็นหลักเพื่อตอบรับ Railway
    port = int(os.environ.get('PORT', 8080)) # ปรับตามที่ Logs ของคุณแสดงคือ 8080
    app.run(host='0.0.0.0', port=port)
