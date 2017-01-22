##该模块实现下载器的代码
import urllib.request
import re

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return

        ##改进->打开网页，获取网页内容
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0')
        response = urllib.request.urlopen(req)

        ##判断获取的getcode是否是200
        if response.getcode() != 200:
            print("获取的getcode不是200,请求失败")
            return None

        ##请求成功,返回
        return response.read().decode('utf-8')

