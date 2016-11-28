import re

import htmldownloader
import htmlparser
from crawler import Crawler


class QCWYCrawler(Crawler):
    def get_url(self):
        url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=280800%2C280200%2C280400%2C00&district=000000&funtype=2600%2C2500%2C0100&industrytype=01%2C38%2C32&issuedate=9&providesalary=99&keywordtype=2&curr_page=1&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
        downloader = htmldownloader.HtmlDownLoader(url)
        html_cont = downloader.download()
        parser = htmlparser.HtmlParser(html_cont)
        soup = parser.get_soup()
        max_page = soup.find("div", class_="dw_page").find("span", class_="td").get_text()
        max_page = int(re.sub("\D", "", max_page))
        # print(max_page)
        curr_page = 1
        urls = []
        while curr_page <= max_page:
            urls.append(re.sub("curr_page=\d", "curr_page=%d" % curr_page, url))
            curr_page += 1
        print('...got %d pages about job info from 51job' % len(urls))
        return urls

    def craw(self):
        print('crawling job info from 51job')
        for url in self.get_url():
            downloader = htmldownloader.HtmlDownLoader(url)
            html_cont = downloader.download()
            parser = htmlparser.HtmlParser(html_cont)
            soup = parser.get_soup()
            items = soup.find("div", {"id": "resultList"}).find_all("div", class_="el")
            items.remove(items[0])
            for item in items:
                tmp_dict = {}
                tmp_dict['media'] = '前程无忧'
                tmp_dict['jobname'] = item.find("p", class_="t1").find("a").get_text().strip()
                tmp_dict['joblink'] = item.find("p", class_="t1").find("a").get("href")
                tmp_dict['company'] = item.find("span", class_="t2").find("a").get_text()
                tmp_dict['location'] = item.find("span", class_="t3").get_text()
                tmp_dict['salary'] = item.find("span", class_="t4").get_text()
                self.data.append(tmp_dict)
        print('...got %d job info items from 51job' % len(self.data))
        print(self.data)
        return self.data
