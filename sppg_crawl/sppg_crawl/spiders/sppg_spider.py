import scrapy


class SppgSpiderSpider(scrapy.Spider):
    name = "sppg_spider"
    allowed_domains = ["bgn.go.id"]
    start_urls = [f"https://bgn.go.id/operasional-sppg?page={i}&search=" 
                  for i in range(1, 2765)]

    def parse(self, response):
        tables = response.css('tr.divide-x')
        for table in tables:
            yield{
                'No': table.css('td:nth-child(1)::text').get(),
                'Provinsi SPPG': table.css('td:nth-child(2)::text').get(),
                'Kab./Kota SPPG': table.css('td:nth-child(3)::text').get(),
                'Kecamatan SPPG': table.css('td:nth-child(4)::text').get(),
                'Kelurahan/Desa SPPG': table.css('td:nth-child(5)::text').get(),
                'Alamat SPPG': table.css('td:nth-child(6)::text').get(),
                'Nama SPPG': table.css('td:nth-child(7)::text').get(),
            }