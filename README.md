conference-crawler
==================

###About

Crawler built with [Scrapy](http://scrapy.org/). Scrapes 1900+ attendees at [openstacksummit.org](http://openstacksummitnovember2014paris.sched.org/directory/attendees).
Also included csv, json and xml files with populated fields of each individual attender such as: name, image url, friends, title, company, location, links, about.

###Screenshot

![Screenshot](http://i.imgur.com/Z85Gaxn.png)

### Installation and Running
```
git clone https://github.com/Lazar-T/conference-crawler
cd conference-crawler
scrapy crawl itemspider
```


