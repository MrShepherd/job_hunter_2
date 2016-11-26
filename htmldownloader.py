from urllib import request


class HtmlDownLoader(object):
    def __init__(self, url):
        self.url = url

    def download(self):
        user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
        headers = {'User-Agent': user_agent}
        req = request.Request(self.url, headers=headers)
        response = request.urlopen(req)
        if response.getcode() == 200:
            return response.read()
