import scrapy
from scrapy_playwright.page import PageMethod


class BerkSpiderSpider(scrapy.Spider):
    name = "berk_spider"
    
    def start_requests(self):
        yield scrapy.Request('https://www.bhhsamb.com/roster/Agents', 
            meta = dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_coroutines=[
                    PageMethod('wait_for_selector', 'div#rosterResults')
                ]
            )
        )

    async def parse(self, response):
        yield {
            'text': response.text
        }