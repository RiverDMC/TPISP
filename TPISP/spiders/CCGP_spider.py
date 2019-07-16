import scrapy

class CCGPSpiderXPath(scrapy.Spider):
    name = 'CCGP-spider'

    def start_requests(self):
        urls = [
            'http://www.ccgp-sichuan.gov.cn/CmsNewsController.do?method=search&years=2018&chnlNames=&chnlCodes=&title=&tenderno=&agentname=&buyername=&startTime=&endTime=&distin_like=510700&province=510000&provinceText=\u56DB\u5DDD\u7701&city=510700&town=&cityText=\u7EF5\u9633\u5E02&townText=\u8BF7\u9009\u62E9&pageSize=10&searchResultForm=search_result_anhui.ftl'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        info_lists = response.xpath('//div[@class="info"]/ul/li')
        for index,info_list in enumerate(info_lists):
            time_curr = info_list.xpath('div[@class="time curr"]').re(r'([0-9][0-9]{1,3})')
            date = time_curr[0]
            years = time_curr[1]
            months = time_curr[2]
            title = info_list.xpath('//div[@class="title"]/text()').get()
            print(dict(
                time=years + "-" + months + "-" + date,
                text=title
            ))



