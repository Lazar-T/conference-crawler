# -*- coding: utf-8 -*-
import urlparse

from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import Compose, MapCompose
from w3lib.html import replace_escape_chars, remove_tags

from openStack.items import ItemloadItem


class ItemspiderSpider(CrawlSpider):
    name = 'openstack'
    allowed_domains = ['openstacksummitnovember2014paris.sched.org']
    start_urls = ['http://openstacksummitnovember2014paris.sched.org/directory/attendees/']

    rules = (
        Rule(LinkExtractor(allow=('/directory/attendees/\d+')),
             callback='parse_page', follow=True),)

    def parse_page(self, response):
        """Yields all attendee urls.

        @url http://openstacksummitnovember2014paris.sched.org/directory/attendees/
        @scrapes attendees

        """
        attendees = response.xpath('//h2/a/@href').extract()
        for attendee in attendees:
            yield Request(urlparse.urljoin(response.url, attendee),
                          callback=self.parse_item)

    def parse_item(self, response):
        """ Returns fields from each individual attendee.

        @url http://openstacksummitnovember2014paris.sched.org/cfb
        @scrapes name image_url friends title_company_location links about

        """
        l = ItemLoader(item=ItemloadItem(), response=response)
        l.default_output_processor = MapCompose(lambda v: v.strip(), replace_escape_chars)

        l.add_xpath('name', '//*[@id="sched-page-me-name"]/text()')
        l.add_xpath('image_url', '//*[@id="myavatar"]/@src')
        l.add_xpath('friends', '//*[@id="sched-page-me-connections"]/ul/li/a/@title')
        l.add_xpath('title_company_location', '//*[@id="sched-page-me-profile-data"]/text()')
        l.add_xpath('links', '//*[@class="sched-network-link"]/a/@href')
        l.add_xpath('about', '//*[@id="sched-page-me-profile-about"]/text()')

        return l.load_item()
