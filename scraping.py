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
        # print(response.url) # Cek apakah ada error atau tidak
        
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

  

# from pathlib import Path

# import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"

#     def start_requests(self):
#         urls = [
#             'https://top-1000-sekolah.ltmpt.ac.id/?page=1&per-page=100',
#             'https://top-1000-sekolah.ltmpt.ac.id/?page=2&per-page=100',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         for sekolah in response.css(f"#w0 > table > tbody"):
#             for x in range(1, 101):
#                 yield {
#                     "npsn":sekolah.css(f"tr:nth-child({str(x)}) > td:nth-child(3) \
#                                         ::text").extract(),
#                     "nama_sekolah":sekolah.css(f"tr:nth-child({str(x)}) > td:nth-child(4) \
#                                                 ::text").extract(),
#                     "nilai_total":sekolah.css(f"tr:nth-child({str(x)}) > td:nth-child(5) \
#                                             ::text").extract(),
#                     "provinsi":sekolah.css(f"tr:nth-child({str(x)}) > td:nth-child(6) \
#                                             ::text").extract(),
#                     "kota/kab":sekolah.css(f"tr:nth-child({(str(x))}) > td:nth-child(7) \
#                                             ::text").extract(),
#                     "jenis_sekolah":sekolah.css(f"tr:nth-child({str(x)}) > td:nth-child(8) \
#                                                 ::text").extract(),
#                 }  
