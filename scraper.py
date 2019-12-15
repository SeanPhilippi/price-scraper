# http library
import requests
from bs4 import BeautifulSoup
# defines an SMTP (simple mail transfer protocol) client session object that can be
# used to send mail to any internet machine using SMTP or ESMTP listener daemon
import smtplib
import time

# setting url of product url I want to watch in const var URL
URL = 'https://www.amazon.com/gp/product/B01C9KG8IG/ref=ox_sc_act_title_1?smid=A191AP80363DWZ&psc=1'
# setting headers object with user agent (browser) info to headers variable
headers = {
  "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}

product = 'Roost laptop stand'
DESIRED_PRICE = 51.00
# wrap below code into a function
def check_price():
  # get request call to url with headers set, stored in var page
  # looks like a bunch of static html data
  page = requests.get(URL, headers=headers)
  # .content gets page res body as bytes,
  # the 2nd paramter is for selecting a parser. lxml is a Python library that allows for easy handling of XML and HTML files, and web scraping
  soup = BeautifulSoup(page.content, 'lxml')

  # store text from element with id productTitle in title var
  if soup.find(id="productTitle").__len__() > 0:
    title = soup.find(id= "productTitle").get_text().strip()
    print(title)
  else:
    title = "No result"
    print(title)
  title = soup.find(id="productTitle").get_text()
  # grab price text from document element
  price = soup.find(id="priceblock_ourprice").get_text()
  # slice the string from the dollar sign to isolate the number, convert to a float
  converted_price = float(price[1:])

  print('title', title.strip())
  print('current price', converted_price)

  if(converted_price < DESIRED_PRICE):
    send_mail()

def send_mail():
  # plugging in host and port number to SMTP function to create server
  server = smtplib.SMTP('smtp.gmail.com', 587)
  # identifying myself as an ESMTP server using EHLO (extended HELO)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('sean.philippi@gmail.com', 'malibwtcdovpdheb')

  subject = f'Price of {product} dropped below {DESIRED_PRICE}!'
  body = f'visit Amazon link here: {URL}'
  msg = f"Subject: {subject}\n\n{body}" # plug subject and body into msg var

  server.sendmail(
    'sean@austincodingacademy.com', # from
    'sean.philippi@gmail.com', # to
    msg # message to send
  )
  print('EMAIL SENT!')
  server.quit()

while(True): # infinite loop
  check_price()
  time.sleep(86400) # pause for amount of seconds in a day