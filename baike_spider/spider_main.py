# -*- coding: utf-8 -*-
from baike_spider import url_manager, html_downloader, html_parser, outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()                  # url管理器
        self.downloader = html_downloader.HtmlDownloader()    # html下载器
        self.parser = html_parser.HtmlParser()                # html解析器
        self.outputer = outputer.HtmlOutputer()               # 数据导出

    def craw(self, root_url):
        count =1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                # 设置爬取的页面数
                if count == 10:
                    break
                count = count+1
            except:
                print 'craw faild'
        self.outputer.output_html()


if __name__ == "__main__":
    # 爬虫的入口url
    root_url = "http://baike.baidu.com/item/python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
