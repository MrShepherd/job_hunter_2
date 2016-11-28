import re

import time

import htmldownloader
import htmlparser
from crawler import Crawler


class GJCrawler(Crawler):
    def get_url(self):
        url = ['http://eerduosi.ganji.com/zpjisuanjiwangluo/o1/', 'http://nmg.ganji.com/zpjisuanjiwangluo/o1/', 'http://baotou.ganji.com/zpjisuanjiwangluo/o1/']
        urls = []
        for item in url:
            curr_page = 1
            max_page = 10
            while curr_page <= max_page:
                urls.append(re.sub("o\d", "o%d" % curr_page, item))
                curr_page += 1
        print('...got %d pages about job info from ganji' % len(urls))
        return urls

    def craw(self):
        print('crawling job info from ganji')
        for url in self.get_url():
            downloader = htmldownloader.HtmlDownLoader(url)
            html_cont = downloader.download()
            parser = htmlparser.HtmlParser(html_cont)
            soup = parser.get_soup()
            items = soup.select("dl.list-noimg.job-list")
            for item in items:
                tmp_dict = {}
                tmp_dict['media'] = '赶集'
                tmp_dict['jobname'] = item.find("dt").find("a").get_text().strip()
                tmp_dict['joblink'] = item.find("dt").find("a").get("href")
                tmp_dict['company'] = item.find("dd", class_="company").find("a").get_text()
                tmp_dict['location'] = item.find("dd", class_="pay").get_text()
                tmp_dict['salary'] = '未知'
                self.data.append(tmp_dict)
            time.sleep(3)
        print('...got %d job info items from ganji' % len(self.data))
        print(self.data)
        return self.data
