import scrapy
import os
import sys
import re

# Set some global variable
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
        urls = ['http://www.12371.cn/']
        for url in urls:
            yield scrapy.Request(url=url,
                                 callback=self.parse)  # 爬取到的页面如何处理？提交给parse方法处理

    def parse(self, response):
        # 根据上面的链接提取分页,如：/page/1/，提取到的就是：1
        block, page = response.url.split("/")[-2:]
        filename = 'dj-%s-%s.html' % (block, page)
        urls = response.xpath("//@href").extract()

        with open(filename, 'wt', encoding="utf-8") as f:  # python文件操作，不多说了；
            # Delete repeat
            urls = list(set(urls))
            for url in urls:
                tempURL = re3.findall(url)
                if tempURL == []:
                    continue
                for i in range(len(tempURL)):
                    if "12371" in str(tempURL[i]).split("."):
                        if tempURL[i].endswith(tuple(ext_search)):
                            # Continue search
                            f.write("%s\n" % (tempURL[i]))
                            yield scrapy.Request(url=tempURL[i], callback=self.parse)
                        elif tempURL[i].endswith(tuple(ext)):
                            # Spider it
                            pass

        self.log('保存文件: %s' % filename)  # 打个日志
