import scrapy

class JobScraperItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    contract_type = scrapy.Field()
    date_posted = scrapy.Field()
    link = scrapy.Field()
