Teknik web scrapping python

Jalankan dengan perintah

```
scrapy runspider scraping.py
```

```
scrapy runspider scraping.py -O latihan.csv
```
-O  = output file (csv, json) 


Untuk masuk ke shell
```
scrapy shell
```
##### response.css("::text").get()   ( Tambhakan ::text untuk mengekstrak teks original )
atau jika masih tidak bisa bisa menggunakan xpath
##### response.xpath("/text()").get() ( Tambahkan /text() untuk mengekstrak teks original )
