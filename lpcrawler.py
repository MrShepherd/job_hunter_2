import time

import htmldownloader
import htmlparser
import re
from crawler import Crawler


class LPCrawler(Crawler):
    def get_url(self):
        url = 'https://www.liepin.com/zhaopin/?industries=&dqs=220&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=&searchType=1&clean_condition=&isAnalysis=&init=-1&sortFlag=15&fromSearchBtn=2&headckid=cf2b01a01fa858b6&key=&jobTitles=360320,360321,100190&ckid=cf2b01a01fa858b6&curPage=1'
        urls = []
        urls.append('https://www.liepin.com/zhaopin/?industries=&dqs=220&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=&searchType=1&clean_condition=&isAnalysis=&init=1&sortFlag=15&fromSearchBtn=1&headckid=e5366aed63bf2c7b&key=')
        max_page = 1
        curr_page = 10
        while curr_page <= max_page:
            urls.append(re.sub("curPage=\d", "curPage=%d" % curr_page, url))
            curr_page += 1
        print('...got %d pages about job info from liepin' % len(urls))
        return urls

    def craw(self):
        print('crawling job info from liepin')
        for url in self.get_url():
            downloader = htmldownloader.HtmlDownLoader(url)
            html_cont = downloader.download()
            # print(html_cont.decode('utf-8'))
            parser = htmlparser.HtmlParser(html_cont)
            soup = parser.get_soup()
            items = soup.find("div", {"class": "sojob-result"}).find_all("li")
            for item in items:
                tmp_dict = {}
                tmp_dict['media'] = '猎聘'
                tmp_dict['jobname'] = item.find("div", class_="job-info").find(["span", "h3"]).get("title")
                tmp_dict['joblink'] = item.find("div", class_="job-info").find(["span", "h3"]).find("a").get("href")
                tmp_dict['company'] = item.find("div", class_="company-info").find("p", class_="company-name").find("a").get_text().strip()
                tmp_dict['location'] = item.find("div", class_="job-info").find("p", class_="condition").find("a", class_="area").get_text().strip()
                tmp_dict['salary'] = item.find("div", class_="job-info").find("p", class_="condition").find("span", class_="text-warning").get_text().strip()
                self.data.append(tmp_dict)
            time.sleep(5)
        print('...got %d job info items from liepin' % len(self.data))
        print(self.data)
        return self.data
