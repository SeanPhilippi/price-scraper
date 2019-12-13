import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/gp/product/B01C9KG8IG/ref=ox_sc_act_title_1?smid=A191AP80363DWZ&psc=1'

headers = {
  "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())