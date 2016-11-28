import sqlite3
from datetime import datetime

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        conn = sqlite3.connect("../data.db")
        cursor = conn.cursor()
        today = datetime.now().strftime("%Y-%m-%d")
        # cursor.execute("SELECT * FROM jobinfo WHERE etldate='%s' order by media" % today)
        cursor.execute("SELECT * FROM jobinfo WHERE etldate='%s' and (location like '%s' or location like '%s' or location like '%s') order by media" % (today, '%鄂尔多斯%', '%东胜%', '%康巴什%'))
        data = cursor.fetchall()[0:50]
        conn.close()
        return render_template('index.html', data=data)
    if request.method == 'POST':
        page = int(request.form.get('page'))
        startindex = 50 * page
        endindex = startindex + 50
        conn = sqlite3.connect("../data.db")
        cursor = conn.cursor()
        today = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("SELECT * FROM jobinfo WHERE etldate='%s' and (location like '%s' or location like '%s' or location like '%s') order by media" % (today, '%鄂尔多斯%', '%东胜%', '%康巴什%'))
        data = cursor.fetchall()[startindex:endindex]
        conn.close()
        return render_template('table.html', data=data)


if __name__ == '__main__':
    app.run(host='192.168.1.102', port=80, debug=True)
