# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import scrapy
from itemadapter import ItemAdapter

# class ImgSpiderPipeline:
#     def open_spider(self, spider):
#         print('爬虫开始')
#
#     def process_item(self, item, spider):
#         src = item["url"]
#         name = src.split("/")[-1]
#         name2 = name.split("?")[0]
#         print('正在保存{}'.format(src))
#         resp = requests.get(url=src).content
#         file_path = "C:/Users/xiaoyang/Documents/python学习区/python学习/python爬虫课程/img_spider/图片"
#         request.urlretrieve(src, file_path + "/" + name)
#
#     def close_spider(self, spider):
#         print('爬虫关闭')
from scrapy.pipelines.images import ImagesPipeline

class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print(item)
        yield scrapy.Request(item["url"])

    def file_path(self, request, response=None, info=None, *, item=None):
        img_name = request.url.split("/")[-1].split("?")[0]
        return img_name

    def item_completed(self, results, item, info):
        return item
