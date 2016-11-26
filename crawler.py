import htmldownloader
import htmlparser


class Crawler(object):
    def __init__(self):
        self.url = ''
        self.base_url = ''
        self.downloader = htmldownloader.HtmlDownLoader(self.url)
        self.html_cont = self.downloader.download()
        self.parser = htmlparser.HtmlParser(self.html_cont)
        self.soup = self.parser.get_soup()
        self.data = []

    def craw(self):
        pass
