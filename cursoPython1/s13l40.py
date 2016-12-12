import bs4
import requests

res = requests.get(
    'https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?s=books&ie=UTF8&qid=1480642453&sr=1-1&keywords=automate+the+boring+stuff+with+python')
print(res.raise_for_status())  # None significa que no hubieron excepciones, o sea OK.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
price = soup.select(
    '#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
print(price[:])
'''
res = requests.get('http://www.taringa.net/')
print(res.raise_for_status())  # None significa que no hubieron excepciones, o sea OK.
soup = bs4.BeautifulSoup(res.text,'html.parser')
print(soup.select('#page > div:nth-of-type(4) > div > main > section.content-left > div > ul > li:nth-of-type(1)'))
'''
