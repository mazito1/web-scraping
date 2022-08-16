import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for i, films in enumerate(response.css(".titleColumn")):
            yield{
                "title"  : films.css(".titleColumn a::text").get(),
                "date" : films.css(".secondaryInfo::text").get()[1:-1],
                "rate" : response.css("strong::text").getall()[i]
            }


