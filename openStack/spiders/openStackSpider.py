# -*- coding: utf-8 -*-
import scrapy
from openStack.items import ItemloadItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Compose, MapCompose
from w3lib.html import replace_escape_chars, remove_tags
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.selector import Selector
import urlparse


class ItemspiderSpider(CrawlSpider):
    name = "itemspider"
    allowed_domains = ["openstacksummitnovember2014paris.sched.org"]
    start_urls = [
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/1',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/2',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/3',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/4',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/5',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/6',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/7',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/8',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/9',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/10',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/11',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/12',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/13',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/14',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/15',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/16',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/17',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/18',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/19',
        'http://openstacksummitnovember2014paris.sched.org/directory/attendees/20',


    ]

    def parse(self, response):
        hxs = Selector(response)
        item_selector = hxs.xpath('//h2/a/@href').extract()
        for url in item_selector:
            yield Request(urlparse.urljoin(response.url, url),
                          callback=self.parse_item)



    def parse_item(self, response):
        l = ItemLoader(item=ItemloadItem(), response=response)
        l.default_output_processor = MapCompose(lambda v: v.strip(), replace_escape_chars)
        l.add_xpath('name', '//*[@id="sched-page-me-name"]/text()')
        l.add_xpath('image_url', '//*[@id="myavatar"]/@src')
        l.add_xpath('friends', '//*[@id="sched-page-me-connections"]/ul/li/a/@title')
        l.add_xpath('title_company_location', '//*[@id="sched-page-me-profile-data"]/text()')
        l.add_xpath('links', '//*[@class="sched-network-link"]/a/@href')
        l.add_xpath('about', '//*[@id="sched-page-me-profile-about"]/text()')
        return l.load_item()
