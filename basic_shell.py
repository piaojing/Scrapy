######### shell scrapy commnad ###########
'''
<ul class="nhsuk-list nhsuk-list--border">
        
        <li>
          <a href="/conditions/abdominal-aortic-aneurysm-screening/">
            AAA screening, see Abdominal aortic aneurysm screening
          </a>
        </li>
'''

# run scrapy shell
# >>> scrapy shell

# input target url
# >>> fetch('https://www.nhs.uk/')

# check response
# >>> response

#  get all elements list by css --- 중요: css선택자에 공백이 있으면 점으로 이어준다.
# >>> response.css('ul.nhsuk-list.nhsuk-list--border') # output -> list type

#  get first element as str type
# >>> response.css('ul.nhsuk-list.nhsuk-list--border').get() # output -> str

# define variable
# >>> t= response.css('ul.nhsuk-list.nhsuk-list--border') # t is List

# get info in t -> output is str
# >>> t.css('a::text').get()  # get first 
# >>> t.css('a::text').getall() # get all


# href목록만 얻어내기
# >>> t.css('a').xpath('@href').get()
# second way
# >>> t.css('a').attrib['href']
# >>> 

