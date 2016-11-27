import sqlite3
from datetime import datetime


class DBHandler(object):
    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        self.today = datetime.now().strftime("%Y-%m-%d")

    def get_all_link(self):
        self.cursor.execute('SELECT joblink FROM jobinfo')
        return self.cursor.fetchall()

    def in_db(self, url):
        return (url,) in self.get_all_link()

    def savedata(self, data):
        for item in data:
            if not self.in_db(item['joblink']):
                item['etldate'] = self.today
                self.cursor.execute("INSERT INTO jobinfo VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
                    item['media'], item['jobname'], item['joblink'], item['company'], item['location'], item['salary'], item['etldate']))
        self.conn.commit()

    def getdata(self):
        self.cursor.execute("SELECT * FROM jobinfo WHERE etldate='%s'" % self.today)
        return self.cursor.fetchall()
