# http library
import requests
# library for pulling data out of html and xml files
from bs4 import BeautifulSoup

# setting url of product url I want to watch in const var URL
URL = 'https://www.amazon.com/gp/product/B01C9KG8IG/ref=ox_sc_act_title_1?smid=A191AP80363DWZ&psc=1'
# setting headers object with user agent (browser) info to headers variable
headers = {
  "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}
# get request call to url with headers set, stored in var page
# looks like a bunch of static html data
page = requests.get(URL, headers=headers)
# .content gets page res body as bytes,
# the 2nd paramter is for selecting a parser.  html.parser comes from Python
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())