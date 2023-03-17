from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://top-1000-sekolah.ltmpt.ac.id/?page=1&per-page=100',
            'https://top-1000-sekolah.ltmpt.ac.id/?page=2&per-page=100',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            "npsn":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(3) \
                                ::text").extract(),
            "nama_sekolah":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(4) \
                                        ::text").extract(),
            "nilai_total":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(5) \
                                       ::text").extract(),
            "provinsi":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(6) \
                                    ::text").extract(),
            "kota/kab":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(7) \
                                    ::text").extract(),
            "jenis_sekolah":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(8) \
                                         ::text").extract(),  
        }
