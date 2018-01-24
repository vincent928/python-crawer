# -*- coding: utf-8 -*-
# url管理器


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):     # 添加新的url
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):    # 添加批量的url
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):               # 判断url管理器中是否还有url
        return len(self.new_urls) != 0

    def get_new_url(self):               # 得到新的url
        new_url = self.new_urls.pop()    # pop()取得set集合中的元素,并删掉该元素
        self.old_urls.add(new_url)
        return new_url


