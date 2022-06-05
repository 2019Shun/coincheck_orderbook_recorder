from PostgreConnect import PostgreConnect
import requests
import json
import os
import signal
from time import sleep
import traceback
import datetime

ORDERBOOK_URL = 'https://coincheck.com/api/order_books'
TICKER_URL = 'https://coincheck.com/api/ticker'
RATE_URL = 'https://coincheck.com/api/rate/btc_jpy'

db_ipaddress = os.environ['DB_IPADDRESS']
db_name = os.environ['DB_NAME']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']

def task(arg1, arg2):
    try:
        # 情報の取得
        btc_orderbook = requests.get(ORDERBOOK_URL).json()
        btc_ticker = requests.get(TICKER_URL).json()
        btc_rate = requests.get(RATE_URL).json()

        #DBへの接続とデータ挿入
        db = PostgreConnect(db_ipaddress, db_name, 'public', db_user, db_password)
        db.execute('insert into btc_orderbook_table (orderbook, ticker, rate, created_at) \
            values (\'' + json.dumps(btc_orderbook)+ '\', \'' + json.dumps(btc_ticker)+ '\', \'' + json.dumps(btc_rate)+ '\', current_timestamp(0))')
            
    except Exception as e:
        print()
        print(datetime.datetime.now())
        print()
        print(e)
        print(traceback.format_exc())


# スケジュール登録
signal.signal(signal.SIGALRM, task)
signal.setitimer(signal.ITIMER_REAL, 10, 10)

# イベント実行
while True:
    sleep(1)