import requests
from bs4 import BeautifulSoup as bs
r = requests.get("https://www.olx.kz/elektronika/kompyutery-i-komplektuyuschie")
html = bs(r.content, 'html.parser')
for el in html.select(".css-1apmciz"):
    title = el.select(".css-u2ayx9 > .css-1tqlkj0 > h4")
    price = el.select(".css-u2ayx9 > .css-uj7mm0")
    address = el.select(".css-odp1qd > .css-vbz67q")
    print(f"[!] {title[0].text} [/] {price[0].text} [\\] {address[0].text} [!]")