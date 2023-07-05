from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        
        # urls = [
        #     "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DInfinix&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.brand%255B%255D%3Dvivo&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.brand%255B%255D%3DASUS&p%5B%5D=facets.brand%255B%255D%3DLenovo&p%5B%5D=facets.brand%255B%255D%3DHuawei&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DLAVA&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DAcer&p%5B%5D=facets.brand%255B%255D%3DIQOO&p%5B%5D=facets.brand%255B%255D%3DI%2BKall&p%5B%5D=facets.brand%255B%255D%3Ditel&p%5B%5D=facets.brand%255B%255D%3DTecno&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DKechaoda&p%5B%5D=facets.brand%255B%255D%3DKARBONN&p%5B%5D=facets.brand%255B%255D%3DNothing&p%5B%5D=facets.brand%255B%255D%3DCellecor&p%5B%5D=facets.brand%255B%255D%3DXOLO&p%5B%5D=facets.brand%255B%255D%3DHTC&p%5B%5D=facets.brand%255B%255D%3DSAREGAMA&p%5B%5D=facets.brand%255B%255D%3DMTR&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DGIONEE&p%5B%5D=facets.brand%255B%255D%3DMicromax&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.brand%255B%255D%3DSnexian&p%5B%5D=facets.brand%255B%255D%3DIAIR&p%5B%5D=facets.brand%255B%255D%3DAlcatel&p%5B%5D=facets.brand%255B%255D%3DEasyfone&p%5B%5D=facets.brand%255B%255D%3DSony%2BEricsson&p%5B%5D=facets.brand%255B%255D%3DYU&p%5B%5D=facets.brand%255B%255D%3DLvix&p%5B%5D=facets.brand%255B%255D%3DGood%2BOne&p%5B%5D=facets.brand%255B%255D%3DMuphone&p%5B%5D=facets.brand%255B%255D%3DTork&p%5B%5D=facets.brand%255B%255D%3DBlackZone&p%5B%5D=facets.brand%255B%255D%3DNubia&p%5B%5D=facets.brand%255B%255D%3DSPICE&p%5B%5D=facets.brand%255B%255D%3Dmobiistar&p%5B%5D=facets.brand%255B%255D%3DIntex&p%5B%5D=facets.brand%255B%255D%3DVideocon&p%5B%5D=facets.brand%255B%255D%3DANGAGE&page=1",
        #     "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DInfinix&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.brand%255B%255D%3Dvivo&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.brand%255B%255D%3DASUS&p%5B%5D=facets.brand%255B%255D%3DLenovo&p%5B%5D=facets.brand%255B%255D%3DHuawei&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DLAVA&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DAcer&p%5B%5D=facets.brand%255B%255D%3DIQOO&p%5B%5D=facets.brand%255B%255D%3DI%2BKall&p%5B%5D=facets.brand%255B%255D%3Ditel&p%5B%5D=facets.brand%255B%255D%3DTecno&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DKechaoda&p%5B%5D=facets.brand%255B%255D%3DKARBONN&p%5B%5D=facets.brand%255B%255D%3DNothing&p%5B%5D=facets.brand%255B%255D%3DCellecor&p%5B%5D=facets.brand%255B%255D%3DXOLO&p%5B%5D=facets.brand%255B%255D%3DHTC&p%5B%5D=facets.brand%255B%255D%3DSAREGAMA&p%5B%5D=facets.brand%255B%255D%3DMTR&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DGIONEE&p%5B%5D=facets.brand%255B%255D%3DMicromax&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.brand%255B%255D%3DSnexian&p%5B%5D=facets.brand%255B%255D%3DIAIR&p%5B%5D=facets.brand%255B%255D%3DAlcatel&p%5B%5D=facets.brand%255B%255D%3DEasyfone&p%5B%5D=facets.brand%255B%255D%3DSony%2BEricsson&p%5B%5D=facets.brand%255B%255D%3DYU&p%5B%5D=facets.brand%255B%255D%3DLvix&p%5B%5D=facets.brand%255B%255D%3DGood%2BOne&p%5B%5D=facets.brand%255B%255D%3DMuphone&p%5B%5D=facets.brand%255B%255D%3DTork&p%5B%5D=facets.brand%255B%255D%3DBlackZone&p%5B%5D=facets.brand%255B%255D%3DNubia&p%5B%5D=facets.brand%255B%255D%3DSPICE&p%5B%5D=facets.brand%255B%255D%3Dmobiistar&p%5B%5D=facets.brand%255B%255D%3DIntex&p%5B%5D=facets.brand%255B%255D%3DVideocon&p%5B%5D=facets.brand%255B%255D%3DANGAGE&page=2",
        # ]

        h_awal = 1
        h_akhir = 207
        urls = [f"https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DInfinix&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.brand%255B%255D%3Dvivo&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.brand%255B%255D%3DASUS&p%5B%5D=facets.brand%255B%255D%3DLenovo&p%5B%5D=facets.brand%255B%255D%3DHuawei&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DLAVA&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DAcer&p%5B%5D=facets.brand%255B%255D%3DIQOO&p%5B%5D=facets.brand%255B%255D%3DI%2BKall&p%5B%5D=facets.brand%255B%255D%3Ditel&p%5B%5D=facets.brand%255B%255D%3DTecno&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DKechaoda&p%5B%5D=facets.brand%255B%255D%3DKARBONN&p%5B%5D=facets.brand%255B%255D%3DNothing&p%5B%5D=facets.brand%255B%255D%3DCellecor&p%5B%5D=facets.brand%255B%255D%3DXOLO&p%5B%5D=facets.brand%255B%255D%3DHTC&p%5B%5D=facets.brand%255B%255D%3DSAREGAMA&p%5B%5D=facets.brand%255B%255D%3DMTR&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DGIONEE&p%5B%5D=facets.brand%255B%255D%3DMicromax&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.brand%255B%255D%3DSnexian&p%5B%5D=facets.brand%255B%255D%3DIAIR&p%5B%5D=facets.brand%255B%255D%3DAlcatel&p%5B%5D=facets.brand%255B%255D%3DEasyfone&p%5B%5D=facets.brand%255B%255D%3DSony%2BEricsson&p%5B%5D=facets.brand%255B%255D%3DYU&p%5B%5D=facets.brand%255B%255D%3DLvix&p%5B%5D=facets.brand%255B%255D%3DGood%2BOne&p%5B%5D=facets.brand%255B%255D%3DMuphone&p%5B%5D=facets.brand%255B%255D%3DTork&p%5B%5D=facets.brand%255B%255D%3DBlackZone&p%5B%5D=facets.brand%255B%255D%3DNubia&p%5B%5D=facets.brand%255B%255D%3DSPICE&p%5B%5D=facets.brand%255B%255D%3Dmobiistar&p%5B%5D=facets.brand%255B%255D%3DIntex&p%5B%5D=facets.brand%255B%255D%3DVideocon&p%5B%5D=facets.brand%255B%255D%3DANGAGE&page={str(halaman)}" for halaman in range(h_awal, h_akhir)]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.url) # Cek apakah ada error atau tidak
        
        for x in response.css("#container > div > div._36fx1h._6t1WkM._3HqJxg > div > div:nth-child(2)"):
            for y in range(2, 26):
                yield {
                    "nama_barang":x.css(f"div:nth-child({str(y)}) > div > div > div > a > div._3pLy-c.row > div.col.col-7-12 > div._4rR01T::text").extract(),
                    "ratings_barang":x.css(f"div:nth-child({str(y)}) > div > div > div > a > div._3pLy-c.row > div.col.col-7-12 > div.gUuXy- > span._2_R_DZ > span > span:nth-child(1)::text").extract(),
                    "review_barang":x.css(f"div:nth-child({str(y)}) > div > div > div > a > div._3pLy-c.row > div.col.col-7-12 > div.gUuXy- > span._2_R_DZ > span > span:nth-child(3)::text").extract(),
                    "deskripsi_barang":x.css(f"div:nth-child({str(y)}) > div > div > div > a > div._3pLy-c.row > div.col.col-7-12 > div.fMghEO > ul > li:nth-child(1)::text").extract(),
                    "harga_barang":x.css(f"div:nth-child({str(y)}) > div > div > div > a > div._3pLy-c.row > div.col.col-5-12.nlI3QM > div._3tbKJL > div._25b18c > div._30jeq3._1_WHN1::text").extract()
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
#         yield {
#             "npsn":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(3) \
#                                 ::text").extract(),
#             "nama_sekolah":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(4) \
#                                         ::text").extract(),
#             "nilai_total":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(5) \
#                                     ::text").extract(),
#             "provinsi":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(6) \
#                                     ::text").extract(),
#             "kota/kab":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(7) \
#                                     ::text").extract(),
#             "jenis_sekolah":response.css("#w0 > table > tbody >tr:nth-child(1) > td:nth-child(8) \
#                                         ::text").extract(),
#             }






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








# # Fungsi try-except => Jika program try (error) maka except akan dijalankan
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
#         try:
#             yield {
#                 "npsn":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(3) \
#                                     ::text").extract(),
#                 "nama_sekolah":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(4) \
#                                             ::text").extract(),
#                 "nilai_total":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(5) \
#                                         ::text").extract(),
#                 "provinsi":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(6) \
#                                         ::text").extract(),
#                 "kota/kab":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(7) \
#                                         ::text").extract(),
#                 "jenis_sekolah":response.css("#w0 > table > tbody >tr:nth-child(1) > td:nth-child(8) \
#                                             ::text").extract(),
#                 }
#         except:
#             yield {
#                 "npsn":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(3) \
#                                     ::text").extract(),
#                 "nama_sekolah":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(4) \
#                                             ::text").extract(),
#                 "nilai_total":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(5) \
#                                         ::text").extract(),
#                 "provinsi":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(6) \
#                                         ::text").extract(),
#                 "kota/kab":response.css("#w0 > table > tbody > tr:nth-child(1) > td:nth-child(7) \
#                                         ::text").extract(),
#                 "jenis_sekolah":response.css("#w0 > table > tbody >tr:nth-child(1) > td:nth-child(8) \
#                                             ::text").extract(),
#                 }

# Fungsi Next page bisa menggunakan ini
# next_page = response.css("a[diikuti nama class]).attrib["href"]
# if next_page is not None:
#     yield response.follow(next_page, callback=self.parse)
