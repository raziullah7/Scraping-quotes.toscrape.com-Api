import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        json_response = json.loads(response.body)
        quotes = json_response.get('quotes')
        print(quotes)
        
        for quote in quotes:
            yield {
                'author': quote.get('author').get('name'),
                'tags': quote.get('tags'),
                'quotes': quote.get('text'),
            }
