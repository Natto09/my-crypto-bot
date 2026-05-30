import yfinance as yf
import pandas_ta as ta

def analyze():
    # ใช้ yfinance ดึงข้อมูล BTC-USD
    ticker = yf.Ticker("BTC-USD")
    df = ticker.history(period="1d", interval="1h")
    
    # คำนวณ EMA
    df['ema9'] = ta.ema(df['Close'], length=9)
    df['ema21'] = ta.ema(df['Close'], length=21)
    
    price = df['Close'].iloc[-1]
    
    # เช็คเงื่อนไขสัญญาณ
    if df['ema9'].iloc[-1] > df['ema21'].iloc[-1]:
        signal = "BUY"
    else:
        signal = "SELL"
    return signal, price