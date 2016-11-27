import re

import htmldownloader
import htmlparser
from crawler import Crawler


class ZLZPCrawler(Crawler):
    def get_url(self):
        url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&jl=%e9%84%82%e5%b0%94%e5%a4%9a%e6%96%af%2b%e5%91%bc%e5%92%8c%e6%b5%a9%e7%89%b9%2b%e5%8c%85%e5%a4%b4&isadv=0&sg=7149f55af5694b09b2f9dff2cf328df5&p=1'
        curr_page = 1
        max_page = 8
        urls = []
        while curr_page <= max_page:
            urls.append(re.sub("p=\d", "p=%d" % curr_page, url))
            curr_page += 1
        print('...got %d pages about job info from zhilian' % len(urls))
        return urls

    def craw(self):
        print('crawling job info from zhilian')
        for url in self.get_url():
            downloader = htmldownloader.HtmlDownLoader(url)
            html_cont = downloader.download()
            parser = htmlparser.HtmlParser(html_cont)
            soup = parser.get_soup()
            items = soup.find("div", id="newlist_list_content_table").find_all("table", class_="newlist")
            items.remove(items[0])
            for item in items:
                tmp_dict = {}
                tmp_dict['media'] = 'zhilian'
                tmp_dict['jobname'] = item.find("td", class_="zwmc").find("a").get_text().strip()
                tmp_dict['joblink'] = item.find("td", class_="zwmc").find("a").get("href")
                tmp_dict['company'] = item.find("td", class_="gsmc").find("a").get_text().strip()
                tmp_dict['location'] = item.find("td", class_="gzdd").get_text().strip()
                tmp_dict['salary'] = item.find("td", class_="zwyx").get_text().strip()
                self.data.append(tmp_dict)
        print('...got %d job info items from zhilian' % len(self.data))
        print(self.data)
        return self.data
