import requests
import scrapy
import re
import json
from img_spider.items import ImgSpiderItem


class ImgSpider(scrapy.Spider):
    name = 'IMG'
    allowed_domains = ['cn.bing.com']
    start_urls = [
        'https://cn.bing.com/images/search?q=jk%E5%B0%8F%E5%A7%90%E5%A7%90&form=HDRSC2&first=1&tsc=ImageHoverTitle&cw=1177&ch=825']

    # 解析网页图片的url，并写入到items
    def parse(self, response, **kwargs):
        items = ImgSpiderItem()
        data_list = response.xpath('//*[@class="dgControl_list"]/li')
        for data in data_list:
            url_list = data.xpath('./div/div/a/@m').extract()
            for url_dict in url_list:
                items["url"] = ''.join(json.loads(url_dict)["murl"]).replace('\ue000', '').replace('\ue001', '')
                # items["title"] = ''.join(json.loads(url_dict)["t"]).replace('\ue000', '').replace('\ue001', '')
                yield items
