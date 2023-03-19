import scrapy


class LiteracyRateSpider(scrapy.Spider):
    name = "literacy_rate"
    allowed_domains = ['www.worldatlas.com']
    start_urls = ['https://www.worldatlas.com/articles/the-highest-literacy-rates-in-the-world.html']

    def parse(self, response):
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            yield {
                'country_name': row.xpath(".//td[1]/text()").get(),
                'literacy_rate': row.xpath(".//td[2]/text()").get(),
            }

