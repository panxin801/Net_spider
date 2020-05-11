import scrapy
import os
import sys
import re
from bs4 import BeautifulSoup


# Set some global variable
# This re2 used for extract data and chinese chars.
re2 = re.compile(r'[\d{4}\u4e00-\u9fa5\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\d{1,2}\u4e00-\u9fa5\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b{1}\d{1,2}\u4e00-\u9fa5\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b{1}]+')
# re3 is used for url filter
re3 = re.compile(
    r'http[s]?://(?:(?!http[s]?://)[a-zA-Z]|[0-9]|[$\-_@.&+/]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
# Meet will continue spider or search
ext = ['.html', '.shtml']
ext_search = ['/']


class dj(scrapy.Spider):  # 需要继承scrapy.Spider类
    name = "dj"  # 定义蜘蛛名

    def start_requests(self):
        # Define start url
        urls = ['http://www.12371.cn/2019/11/01/ARTI1572574048107450.shtml']
        for url in urls:
            # 爬取到的页面如何处理？提交给parse方法处理
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.body
        soup = BeautifulSoup(data, "html5lib")
        temURL = re3.findall(str(soup))
        temTXT = soup.get_text()
        text = re2.findall(temTXT)
        block, page = response.url.split("/")[-2:]
        filename = 'dj-%s-%s.txt' % (block, page)
        with open(filename, 'wt', encoding='utf-8') as file:
            for i in text:
                if len(i) > 20:
                    file.write('\n' + i)

        if temURL is not None:
            for url in temURL:
                yield scrapy.Request(url, callback=self.parse, dont_filter=False)

        # 根据上面的链接提取分页,如：/page/1/，提取到的就是：1
        # block, page = response.url.split("/")[-2:]
        # filename = 'dj-%s-%s.html' % (block, page)
        # urls = response.xpath("//@href").extract()
        #
        # with open(filename, 'wt', encoding="utf-8") as f:  # python文件操作，不多说了；
        #     # Delete repeat
        #     urls = list(set(urls))
        #     for url in urls:
        #         tempURL = re3.findall(url)
        #         if tempURL == []:
        #             continue
        #         for i in range(len(tempURL)):
        #             if "12371" in str(tempURL[i]).split("."):
        #                 if tempURL[i].endswith(tuple(ext_search)):
        #                     # Continue search
        #                     f.write("%s\n" % (tempURL[i]))
        #                     yield scrapy.Request(url=tempURL[i], callback=self.parse)
        #                 elif tempURL[i].endswith(tuple(ext)):
        #                     # Spider it
        #                     pass
        #
        # self.log('保存文件: %s' % filename)  # 打个日志
