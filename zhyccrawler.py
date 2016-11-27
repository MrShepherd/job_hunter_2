import re

import time

import htmldownloader
import htmlparser
from crawler import Crawler


class ZHYCCrawler(Crawler):
    def get_url(self):
        url = 'http://www.chinahr.com/sou/?orderField=relate&keyword=Java+Python+PHP+.NET+C%23+C%2B%2B+C+Delphi+Perl+Ruby+Hadoop+Node.js+MySQL+SQLServer&city=39,416;39,417;39,421&industrys=1100&page=1'
        downloader = htmldownloader.HtmlDownLoader(url)
        html_cont = downloader.download()
        parser = htmlparser.HtmlParser(html_cont)
        soup = parser.get_soup()
        max_page = int(soup.find("div", class_="pageList").find_all("a")[-2].get_text())
        curr_page = 1
        urls = []
        while curr_page <= max_page:
            urls.append(re.sub("page=\d", "curr_page=%d" % curr_page, url))
            curr_page += 1
        print('...got %d pages about job info from chinahr' % len(urls))
        return urls

    def craw(self):
        print('crawling job info from chinahr')
        for url in self.get_url():
            downloader = htmldownloader.HtmlDownLoader(url)
            html_cont = downloader.download()
            parser = htmlparser.HtmlParser(html_cont)
            soup = parser.get_soup()
            items = soup.find("div", {"class": "resultList"}).find_all("div", class_="jobList")
            for item in items:
                tmp_dict = {}
                tmp_dict['media'] = 'chinahr'
                tmp_dict['jobname'] = item.find("li", class_="l1").find("span", class_="e1").find("a").get_text().strip()
                tmp_dict['joblink'] = item.find("li", class_="l1").find("span", class_="e1").find("a").get("href")
                tmp_dict['company'] = item.find("li", class_="l1").find("span", class_="e3").find("a").get_text().strip()
                tmp_dict['location'] = item.find("li", class_="l2").find("span", class_="e1").get_text().split(']')[0].replace('[', '').strip()
                tmp_dict['salary'] = item.find("li", class_="l2").find("span", class_="e2").get_text().strip()
                self.data.append(tmp_dict)
            time.sleep(3)
        print('...got %d job info items from chinahr' % len(self.data))
        print(self.data)
        return self.data
