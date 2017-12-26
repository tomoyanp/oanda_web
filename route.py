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
from common import getBollingerDataSet
mysql_connector = MysqlConnector()

from flask import Flask, render_template, request, Response


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show-graphic', methods=['GET'])
def showGraphic():

#    instruments = response.instruments
    start_time = request.args.get('starttime')
    end_time = request.args.get('endtime')
    instruments = request.args.get('instruments')
#    sql = "select ask_price, bid_price, insert_time from %s_TABLE where insert_time > \'%s\' and insert_time < \'%s\'" % (instruments, start_time, end_time)
    sql = "select ask_price, bid_price, insert_time from %s_TABLE where insert_time > \'%s\' and insert_time < \'%s\' and insert_time like \'%%0:00\'" % (instruments, start_time, end_time)
    #print sql
    response = mysql_connector.select_sql(sql)
    ask_price_list = []
    bid_price_list = []
    insert_time_list = []

    for elm in response:
        ask_price_list.append(elm[0])
        bid_price_list.append(elm[1])
        insert_time_list.append(elm[2].strftime("%Y-%m-%d %H:%M:%S"))

    window_size = 28
    candle_width = 600
    sigma_valiable = 2
    data_set2 = getBollingerDataSet(ask_price_list, bid_price_list, window_size, sigma_valiable, candle_width)
    upper_sigmas = data_set2["upper_sigmas"]
    lower_sigmas = data_set2["lower_sigmas"]
    base_lines   = data_set2["base_lines"]

    for i in range(0, len(upper_sigmas)):
    if math.isnan(upper_sigmas[i]):
        upper_sigmas[i] = ""
        lower_sigmas[i] = ""
        base_lines[i]   = ""

    response_json = { "ask_price": ask_price_list,
                      "bid_price": bid_price_list,
                      "insert_time": insert_time_list,
                      "upper_sigmas": upper_sigmas,
                      "lower_sigmas": lower_sigmas,
                      "base_lines"  : base_lines}

    print response_json

#    return Response(json.dumps(return_json))
    return Response(json.dumps(response_json))

if __name__ == "__main__":
    app.run(debug=True, host="172.126.97.125")
#    app.run(debug=True, host="160.16.197.5")
