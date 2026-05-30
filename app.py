from flask import Flask, render_template  # 1. เพิ่ม render_template เข้ามา
import threading
import os

app = Flask(__name__)

# ... (ฟังก์ชัน run_bot ของคุณ) ...

@app.route('/')
def home():
    # 2. แก้ตรงนี้: แทนที่จะ return ข้อความ ให้เรียก render_template
    # ส่งข้อมูลตัวอย่างไปที่หน้าเว็บด้วย
    data = {'status': 'Running', 'balance': '100 USD'} 
    return render_template('index.html', data=data)

# ... (ส่วน if __name__ == '__main__' เหมือนเดิม) ...
if __name__ == '__main__':
    # 1. สั่งให้บอทเริ่มทำงานในเบื้องหลัง (Background Thread)
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # 2. ให้ Flask รันเป็นหลักเพื่อตอบรับ Railway
    port = int(os.environ.get('PORT', 8080)) # ปรับตามที่ Logs ของคุณแสดงคือ 8080
    app.run(host='0.0.0.0', port=port)
