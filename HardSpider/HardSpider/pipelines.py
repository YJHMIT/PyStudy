# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os


# 自定义文件写入pipelines
class HardspiderPipeline(object):

    def __init__(self):
        # 打开本地的json文件，W+有的话打开或者直接创建打开
        self.file = codecs.open(filename='douban.json', mode='w+', encoding='utf-8')
        self.file.write('"douban_list":[')

    # 需要将数据写入本地或者数据库中，必用process——item()函数
    def process_item(self, item, spider):
        # 将item对象转化为一个字典对象
        res = dict(item)
        # 再将字典对象转化为json字符串
        str = json.dumps(res, ensure_ascii=False)
        # 写入json字符串
        self.file.write(str)
        # 添加换行符
        self.file.write(',\n')
        # 返回一个item对象，供后续的pipeline对这个item进行处理
        return item

    def open_spider(self, spider):
        # 爬虫开启时，这句话会被输出
        print('爬虫启动')

    def close_spider(self, spider):
        # 爬虫关闭会输出这句话
        print("爬虫关闭")
        """
        将json文件的最后字符',\'删掉
        -1表示偏移量至文件末尾，SEEK_END定位到文章的最后一个字符
        """
        self.file.seek(-1, os.SEEK_END)
        # 去除换行符\n
        self.file.truncate()
        # 去除逗号
        self.file.seek(-1, os.SEEK_END)
        self.file.truncate()
        # 加上列表的另外一部分
        self.file.write(']')
        self.file.close()
