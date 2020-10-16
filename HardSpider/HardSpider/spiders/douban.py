# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from HardSpider.items import AticleItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/note/749100238/']

    def parse(self, response):
        """
        提取文章的具体字段
        1.获取当前文章列表页中的url并下载后交给解析函数进行具体字段的解析
        2.获取下一页的url并交给scrapy进行下载，下载后交给parse函数
        :param response:
        :return:
        """
        # 解析列表页中所有的url文章并交给scrapy下载后进行解析
        # sns_url = response.css("#anony-sns.section div.mod li.rec_topics a.rec_topics_name::attr(href)").extract()
        # for post_url in sns_url:
        #    yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail())
        # 提取下一页url并进行解析
        # time_url=response.css("#anony-time.section div.main ul.time-list li a.title::attr(href)").extract()

    def parse_detail(self, response):
        # css,xpath选择器进行数据筛选
        # 提取文章细节的具体逻辑
        article_item = AticleItem()
        title = response.xpath("//div[@class='note-header note-header-container']/h1/text()").extract()[0]
        print(title)
        date = response.xpath("//span[@class='pub-date']/text()").extract()[0]
        print(date)
        article = response.xpath("//div[@class='note']/p").extract()
        agreement = response.css("span.js-donate-count::text").extract()[0]
        print(agreement)
        tags = response.css("span.rec-num::text").extract()[0]
        print(tags)
        print('-' * 20)
        article_item["title"] = title
        article_item["date"] = date
        article_item["agreement"] = agreement
        article_item["tags"] = tags

        yield article_item
        pass
