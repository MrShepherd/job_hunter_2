import gjcrawler
import lpcrawler
import qcwycrawler
import wbtccrawler
import zhyccrawler
import zlzpcrawler


class Spider(object):
    def __init__(self):
        self.data = []

    def craw(self):
        crawler_obj = qcwycrawler.QCWYCrawler()
        self.data += crawler_obj.craw()
        crawler_obj = wbtccrawler.WBTCCrawler()
        self.data += crawler_obj.craw()
        crawler_obj = zlzpcrawler.ZLZPCrawler()
        self.data += crawler_obj.craw()
        crawler_obj = zhyccrawler.ZHYCCrawler()
        self.data += crawler_obj.craw()
        crawler_obj = gjcrawler.GJCrawler()
        self.data += crawler_obj.craw()
        crawler_obj = lpcrawler.LPCrawler()
        self.data += crawler_obj.craw()
        return self.data
