import time

import htmldownloader
import htmlparser
from crawler import Crawler


class LPCrawler(Crawler):
    def get_url(self):
        urls = [
            'https://www.liepin.com/zhaopin/?industries=&dqs=220050&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=&searchType=1&clean_condition=&isAnalysis=&init=1&sortFlag=15&fromSearchBtn=1&headckid=7fc6d282f8719ed2&key=',
            'https://www.liepin.com/zhaopin/?industries=&dqs=220050&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=&searchType=1&clean_condition=&isAnalysis=&init=-1&sortFlag=15&fromSearchBtn=2&headckid=f66f3b3004fed723&key=&ckid=f66f3b3004fed723&curPage=1',
            'https://www.liepin.com/zhaopin/?industries=040&dqs=220&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=industry_01&searchType=1&clean_condition=&isAnalysis=&init=-1&sortFlag=15&fromSearchBtn=2&headckid=572caf45ca263f8a&key=&ckid=572caf45ca263f8a&flushckid=1',
            'https://www.liepin.com/zhaopin/?industries=040&dqs=220&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=industry_01&searchType=1&clean_condition=&isAnalysis=&init=-1&sortFlag=15&fromSearchBtn=2&head&ckid=31cdc360b70c3ffc&key=&&ckid=31cdc360b70c3ffc&headckid=572caf45ca263f8a&curPage=1',
            'https://www.liepin.com/zhaopin/?industries=040&dqs=220&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=industry_01&searchType=1&clean_condition=&isAnalysis=&init=-1&sortFlag=15&fromSearchBtn=2&head&ckid=31cdc360b70c3ffc&key=&&ckid=31cdc360b70c3ffc&headckid=572caf45ca263f8a&curPage=2',
            'https://www.liepin.com/zhaopin/?industries=010&dqs=220&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=industry_01&searchType=1&clean_condition=&isAnalysis=&init=-1&sortFlag=15&fromSearchBtn=2&head&&ckid=8f0e77326d3b8df4&key=&&&ckid=8f0e77326d3b8df4&headckid=572caf45ca263f8a&curPage=2&flushckid=1',
            'https://www.liepin.com/zhaopin/?industries=010&dqs=220&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=industry_01&searchType=1&clean_condition=&isAnalysis=&init=-1&sortFlag=15&fromSearchBtn=2&head&&&ckid=a95a6beb3bd3e626&key=&&&&ckid=a95a6beb3bd3e626&headckid=572caf45ca263f8a&curPage=1',
            'https://www.liepin.com/zhaopin/?industries=010&dqs=220&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=industry_01&searchType=1&clean_condition=&isAnalysis=&init=-1&sortFlag=15&fromSearchBtn=2&head&&&ckid=a95a6beb3bd3e626&key=&&&&ckid=a95a6beb3bd3e626&headckid=572caf45ca263f8a&curPage=2',
            'https://www.liepin.com/zhaopin/?industries=030&dqs=220&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=industry_01&searchType=1&clean_condition=&isAnalysis=&init=-1&sortFlag=15&fromSearchBtn=2&head&&&ckid=a95a6beb3bd3e626&key=&&&&ckid=a95a6beb3bd3e626&headckid=572caf45ca263f8a&curPage=2&flushckid=1']
        print('...got %d pages about job info from liepin' % len(urls))
        return urls

    def craw(self):
        print('crawling job info from liepin')
        for url in self.get_url():
            downloader = htmldownloader.HtmlDownLoader(url)
            html_cont = downloader.download()
            parser = htmlparser.HtmlParser(html_cont)
            soup = parser.get_soup()
            items = soup.find("div", {"class": "sojob-result"}).find_all("li")
            for item in items:
                tmp_dict = {}
                tmp_dict['media'] = 'liepin'
                tmp_dict['jobname'] = item.find("div", class_="job-info").find(["span", "h3"]).get("title")
                tmp_dict['joblink'] = item.find("div", class_="job-info").find(["span", "h3"]).find("a").get("href")
                tmp_dict['company'] = item.find("div", class_="company-info").find("p", class_="company-name").find("a").get_text().strip()
                tmp_dict['location'] = item.find("div", class_="job-info").find("p", class_="condition").find("a", class_="area").get_text().strip()
                tmp_dict['salary'] = item.find("div", class_="job-info").find("p", class_="condition").find("span", class_="text-warning").get_text().strip()
                self.data.append(tmp_dict)
            time.sleep(3)
        print('...got %d job info items from liepin' % len(self.data))
        print(self.data)
        return self.data
