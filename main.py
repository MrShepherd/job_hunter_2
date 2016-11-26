import crawler
import dbhandler
import htmloutputer

if __name__ == '__main__':
    crawler_obj = crawler.Crawler()
    data_today = crawler_obj.craw()
    dbhandler_obj = dbhandler.DBHandler()
    dbhandler_obj.savedata()
    job_info_new = dbhandler_obj.getdata()
    outputer_obj = htmloutputer.HtmlOutputer()
    outputer_obj.output()
    print('hello')
