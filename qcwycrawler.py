import htmldownloader
import htmlparser
from crawler import Crawler


class QCWYCrawler(Crawler):
    def get_url(self):
        urls = []
        return urls

    def craw(self):
        for url in self.get_url():
            tmp_dict = {}
            downloader = htmldownloader.HtmlDownLoader(url)
            html_cont = downloader.download()
            parser = htmlparser.HtmlParser(html_cont)
            soup = parser.get_soup()
            tmp_dict['tmp'] = soup.find_all()
            self.data.append(tmp_dict)
        return self.data
