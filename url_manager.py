##url管理器

class UrlManager(object):
    ##url管理器需要维护两个列表，一个是爬取过的url，一个是带爬取的url
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    ## 向管理器中添加一个新的url
    def add_new_url(self, url):
        ##首先进行参数的判断
        if url is None:
            return
        ##判断获取的地址是否在新的或已经爬取过的列表里面
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    ## 向管理器中添加批量的url
    def add_new_urls(self, urls):
        ##首先判断urls是否为空
        if urls is None or len(urls) == 0:
            return
        ##调用add_new_url进行单个的添加
        for url in urls:
            self.add_new_url(url)

    ##判断是否有新的url
    def has_new_url(self):
        ##判断这个新表里的数据是否为空
        return len(self.new_urls) != 0

    ## 从管理器中获取一个新的带爬取的url
    def get_new_url(self):
        ##获取一个
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
