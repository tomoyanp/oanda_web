# coding: utf-8

import sys
import os
import traceback
import json
import math

# 実行スクリプトのパスを取得して、追加
current_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_path)
sys.path.append(current_path + "/lib")

from mysql_connector import MysqlConnector
mysql_connector = MysqlConnector()

from flask import Flask, render_template, request, Response

app = Flask(__name__)



def getTradeHistoryDataset(ask_price_list, bid_price_list, insert_time_list)
    trade_list = []
    stl_list = []

    trade_cmp_time = "2017-12-26 03:00:00"
    stl_cmp_time = "2017-12-26 06:00:00"

    for i in range(0, len(insert_time_list)):
        if insert_time_list[i] == trade_cmp_time:
            trade_list.append(ask_price_list[i])
            print ask_price_list[i]
        else:
            trade_list.append(None)

        if insert_time_list[i] == stl_cmp_time:
            stl_list.append(ask_price_list[i])
            print ask_price_list[i]
        else:
            stl_list.append(None)

    return trade_list, stl_list 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show-graphic', methods=['GET'])
def showGraphic():

#    instruments = response.instruments
    start_time = request.args.get('starttime')
    end_time = request.args.get('endtime')
    instruments = request.args.get('instruments')
    sql = "select ask_price, bid_price, insert_time from %s_TABLE where insert_time > \'%s\' and insert_time < \'%s\'" % (instruments, start_time, end_time)
#    sql = "select ask_price, bid_price, insert_time from %s_TABLE where insert_time > \'%s\' and insert_time < \'%s\' and insert_time like \'%%0:00\'" % (instruments, start_time, end_time)
    #print sql
    response = mysql_connector.select_sql(sql)
    ask_price_list = []
    bid_price_list = []
    insert_time_list = []

    for elm in response:
        ask_price_list.append(elm[0])
        bid_price_list.append(elm[1])
        insert_time_list.append(elm[2].strftime("%Y-%m-%d %H:%M:%S"))

       
    trade_list, stl_list = getTradeHistory(ask_price_list, bid_price_list, insert_time_list)
    response_json = { "ask_price": ask_price_list,
                      "bid_price": bid_price_list,
                      "insert_time": insert_time_list,
                      "trade_list": trade_list,
                      "stl_list": stl_list}

#    print response_json

#    return Response(json.dumps(return_json))
    return Response(json.dumps(response_json))

if __name__ == "__main__":
    app.run(debug=True, host="172.126.97.125")
#    app.run(debug=True, host="160.16.197.5")
