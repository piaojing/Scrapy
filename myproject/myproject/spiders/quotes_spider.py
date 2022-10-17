import scrapy


class QuotesSpider(scrapy.Spider):
    name = "nhs-condition"
    start_urls=['https://www.nhs.uk/conditions/']
    
    def parse(self, response):
        letter_list=[]
        for letter in response.css('a.nhsuk-u-font-size-22.nhsuk-u-padding-2.nhsuk-u-display-block'):
            letter_list.append(letter.css('a::text').get())
        print(letter_list)

        first_ul=response.css('ul.nhsuk-list.nhsuk-list--border')
        print('------>',len(first_ul))
        for i in range(len(first_ul)):    
            a_li=first_ul[i].css('a')
            try:
                for t in a_li: # t is List
                    yield {
                        'letter': letter_list[i],
                        'link': t.css('a').attrib['href']
                    }
            except:
                print('Error !!!!!!!')

# scrapy crawl nhs-condition -O quotes.json

# run file directly
# goto project directory and run below cmd
# scrapy runspider nhs.py -o nhs.jl