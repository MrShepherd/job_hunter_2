import re

import time

import htmldownloader
import htmlparser
from crawler import Crawler


class WBTCCrawler(Crawler):
    def get_url(self):
        url = ['http://erds.58.com/tech/pn1/?bd=1&PGTID=0d303655-007f-5843-5383-d45570b65492&ClickID=1', 'http://hu.58.com/tech/pn1/?bd=1&PGTID=0d303655-007f-5843-5383-d45570b65492&ClickID=1',
               'http://bt.58.com/tech/pn1/?bd=1&PGTID=0d303655-007f-5843-5383-d45570b65492&ClickID=1']
        urls = []
        for item in url:
            curr_page = 1
            max_page = 7
            while curr_page <= max_page:
                urls.append(re.sub("pn\d", "pn%d" % curr_page, item))
                curr_page += 1
        print('...got %d pages about job info from 58' % len(urls))
        return urls

    def craw(self):
        print('crawling job info from 58')
        for url in self.get_url():
            downloader = htmldownloader.HtmlDownLoader(url)
            html_cont = downloader.download()
            parser = htmlparser.HtmlParser(html_cont)
            soup = parser.get_soup()
            items = soup.find("div", id="infolist").find_all("dl")
            for item in items:
                tmp_dict = {}
                tmp_dict['media'] = '58'
                tmp_dict['jobname'] = item.find("dt").find("a").get_text().strip()
                tmp_dict['joblink'] = item.find("dt").find("a").get("href")
                tmp_dict['company'] = item.find("dd", class_="w271").find("a").get_text()
                tmp_dict['location'] = item.find("dd", class_="w96").get_text()
                tmp_dict['salary'] = 'unknown'
                self.data.append(tmp_dict)
            time.sleep(3)
        print('...got %d job info items from 58' % len(self.data))
        print(self.data)
        return self.data
