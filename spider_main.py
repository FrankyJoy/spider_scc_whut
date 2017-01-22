#爬虫总调度程序


##编写main函数
from test6 import html_downloader,url_manager,  html_outputer, html_Parser
import os


class SpiderMain(object):
    def __init__(self):
        ##urls 作为下载器
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_Parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        ##
    def craw(self, root_url):
        count = 1  ##记录当前爬取的页面是第几个
        ##添加入口url
        self.urls.add_new_url(root_url)
        ##启动爬虫的循环，当url管理器有带爬取的url的时候
        while self.urls.has_new_url():
            try:

                ##获取一个新的url
                new_url = self.urls.get_new_url()
                ##打印当前爬取的是第几个url
                print("craw %d : %s" % (count,new_url))
                ##获取url之后，启动下载器下载页面，结果存储在html的content中
                html_cont = self.downloader.download(new_url)
                ##下载好了页面,调用url解析器解析，得到新的url列表以及新的数据,传入新爬取的url以及当前页面的数据
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                ##新得到的数据分开处理，url添加进管理器，数据被收集
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                self.outputer.output_html()
                print("Main函数中，count= ",count)
                if count == 30:
                    break
                count = count + 1

            except:
                print('craw failed')

        ##最后调用函数进行输出



if __name__ =="__main__":
    root_url = "http://scc.whut.edu.cn/vjlist.aspx?type=zhaopinginfo&vj"
    os.mkdir('html')
    os.chdir('html')
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)