# -*- coding: utf-8 -*-
import scrapy


class MoviesbotSpider(scrapy.Spider):
    name = 'moviesbot'
    allowed_domains = ['www.imdb.com/chart/moviemeter']
    start_urls = ['https://www.imdb.com/chart/moviemeter']

    def parse(self, response):
        pass
        #Extracting the content using css selectors
        table = response.xpath('//*[@class="lister"]/table//tr')
        for movie in table:
            movie_info = {}
            movie_info['title'] = movie.xpath('td[@class="titleColumn"]/a/text()').extract_first()
            movie_info['rating'] = movie.xpath('td[@class="ratingColumn imdbRating"]/strong/text()').extract_first()
            movie_info['number'] = movie.xpath('td[@class="titleColumn"]/div[@class="velocity"]/text()').extract_first()
            yield movie_info

