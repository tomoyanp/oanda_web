# coding: utf-8

import sys
import os
import traceback
import json

# 実行スクリプトのパスを取得して、追加
current_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_path)
sys.path.append(current_path + "/lib")

#from mysql_connector import MysqlConnector
#mysql_connector = MysqlConnector()

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
    sql = "select ask_price, bid_price, insert_time from %s_TABLE where insert_time > \'%s\' and insert_time < \'%s\'" % (instruments, start_time, end_time)
    print sql
    response = mysql_connector.select_sql(sql)

#    return Response(json.dumps(return_json))
    return Response(start_time)

if __name__ == "__main__":
#    app.run(debug=True, host="160.xxx.xxx.xxx")
    app.run(debug=True)
