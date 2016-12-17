from urllib import request


class HtmlDownLoader(object):
    def __init__(self, url):
        self.url = url

    def download(self):
        user_agent = 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
        headers = {'User-Agent': user_agent}
        req = request.Request(self.url, headers=headers)
        response = request.urlopen(req)
        if response.getcode() == 200:
            return response.read()
