import spider
import dbhandler
import htmloutputer

if __name__ == '__main__':
    crawler_obj = spider.Spider()
    data_today = crawler_obj.craw()
    print('crawler finished,got %d items of job info' % len(data_today))
    dbhandler_obj = dbhandler.DBHandler()
    dbhandler_obj.savedata(data_today)
    job_info_new = dbhandler_obj.getdata()
    print('db task finished,got %d items of new job info today' % len(job_info_new))
    print(job_info_new)
    outputer_obj = htmloutputer.HtmlOutputer(job_info_new)
    outputer_obj.output()
