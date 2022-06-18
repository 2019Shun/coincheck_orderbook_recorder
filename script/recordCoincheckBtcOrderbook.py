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
TABLE_NAME = 'btc_orderbook_table'

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

def task2(arg1, arg2):
    try:
        # 情報の取得
        btc_orderbook = requests.get(ORDERBOOK_URL).json()

        # 文字列を数値へ変換
        for ask_or_bid in ['asks', 'bids']:
            for i in range(len(btc_orderbook[ask_or_bid])):
                btc_orderbook[ask_or_bid][i] = [float(btc_orderbook[ask_or_bid][i][0]), float(btc_orderbook[ask_or_bid][i][1])]

        #DBへの接続とデータ挿入
        db = PostgreConnect(db_ipaddress, db_name, 'public', db_user, db_password)
        db.execute('insert into ' + TABLE_NAME + ' (orderbook, created_at) \
            values (\'' + json.dumps(btc_orderbook) + '\', current_timestamp(3))')
            
    except Exception as e:
        print()
        print(datetime.datetime.now())
        print()
        print(e)
        print()


# スケジュール登録
signal.signal(signal.SIGALRM, task2)
signal.setitimer(signal.ITIMER_REAL, 10, 1)

# イベント実行
while True:
    sleep(10)