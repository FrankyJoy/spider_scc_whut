## 解析器模块，只需要对外提供parse方法
from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        ##新建列表，存放url
        new_urls = set()
        ##网页链接的形式为
        ## vjread.aspx?id=6a77f370-12ca-47cc-846d-554a20dca536&vj 先实现该部分网页抓取
        ## vjlist.aspx?type=zhaopinginfo&=vj&page=2
        links = soup.find_all('a',href=re.compile(r'vjread\.aspx\?id=.{8}-.{4}-.{4}-.{4}-.{0,19}'))
        jumps = soup.find_all('a',href=re.compile(r'vjlist\.aspx\?type=zhaopinginfo&=vj&page=.{1,2}'))
        badStat = 'http://scc.whut.edu.cn/vjread.aspx?id=18df4bec-4673-4d07-b528-3d0c7a63849e&vj'

        for link in links:
            new_url = link['href']
            ##print("html_parser获取的url为",new_url)
            ##将new_url按照 page_url的格式拼接成一个全新的url
            ##new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            ##new_full_url = r"http://scc.whut.edu.cn/"+new_url
            if new_full_url == badStat:  ##抓取了一个坏的声明页
                print("get_new_data抓去一个坏的声明页,该页面已经被放弃。")
            else:
                print("拼接出的新的url为",new_full_url)
                new_urls.add(new_full_url)
        for jump in jumps:
            new_url1 = jump['href']
            new_full_url1 = urllib.parse.urljoin(page_url,new_url1)
            if new_full_url1 == badStat:  ##抓取了一个坏的声明页
                print("get_new_data抓去一个坏的声明页,该页面已经被放弃。")
            else:
                print("jumps拼接出的新的url为", new_full_url1)
                new_urls.add(new_full_url1)
        return new_urls

    ##解析数据，此处暂时只解析title和summary两个数据
    def _get_new_data(self, page_url, soup):
        res_data = {}  ##新建字典
        facepage = 'type=zhaopinginfo'
        if re.search(facepage,page_url) != None:##说明该页面不是信息页面
            print("get_new_data抓取了一个跳转页面： ",page_url,"该页面已经被放弃。")
            return

        res_data['url'] =page_url
        ## <h2 class="nr-tit">
        ##title_node = soup.find_all('h2',class_='nr-tit').text
        ##此处get_text()不可用，在查看源码和文档后使用.title.get_text()
        title_node = soup.title.get_text()

        print("找到的标题为",title_node)
        res_data['title'] = title_node

        ## <div class="Section1">
        cont_node = soup.find_all('div',class_='Section1')
        print(cont_node)
        res_data['summary'] = cont_node
        return res_data

    ##该方法需要我们从html_cont中解析出新的url列表和方法
    def parse(self, page_url, html_cont):
        ##首先进行参数的判断
        if page_url is None or html_cont is None:
            return

        ##将cont加载进beautifulsoup进行解析
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        ##从网页内容中解析出新的网页列表
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data



