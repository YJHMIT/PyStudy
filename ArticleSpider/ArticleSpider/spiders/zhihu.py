# -*- coding: utf-8 -*-
import re
from scrapy.http import Request
import scrapy
from urllib import parse

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/question/368916003/answer/1006910871']

    def parse(self, response):
        """
        提取文章的具体字段
        1.获取当前文章列表页中的url并下载后交给解析函数进行具体字段的解析
        2.获取下一页的url并交给scrapy进行下载，下载后交给parse函数
        :param response:
        :return:
        """

        title = response.xpath("//h1[@class='QuestionHeader-title']/text()").extract_first()
        comment=response.xpath("//button[@class='Button ContentItem-action Button--plain Button--withIcon Button--withLabel']/text()").extract()[0]
        match_re=re.match(".*?(\d+)条评论",comment)
        if match_re:
            comment=match_re.group(1)
        article = response.xpath("//div[@class='RichContent-inner']").extract()[0]

        #通过css选择器进行数据筛选
        agreement1 = response.css("span.Voters button::text").extract()[0]
        match1=re.match(".*?(\d+)人",agreement1)
        if match1:
            agreement1=match1.group(1)
        agreement2 = response.css("div.ContentItem-actions span button::text").extract()[0]
        match2 = re.match(".*?(\d+)", agreement2)
        if match2:
            agreement2 = match2.group(1)
        tag_lists = response.css("div.ContentItem-actions button::text").extract()
        tag_lists = [element for element in tag_lists if not element.strip().endwith("分享","收藏","喜欢")]
        tags= ",".join(tag_lists)
        pass
