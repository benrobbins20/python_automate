#!python3
import bs4
import requests
#TODO make functions for various scraping desires



#https://www.geeksforgeeks.org/scraping-amazon-product-information-using-beautiful-soup/
url = "https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994"
headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
ro = requests.get(url,headers = headers)
ro.raise_for_status()
#parse object
po = bs4.BeautifulSoup(ro.content,'html.parser')
po_pretty = bs4.BeautifulSoup(po.prettify(),'html.parser')

#CSS path 
price = po_pretty.find("span", attrs={'id': 'newBuyBoxPrice'})
print(price.text.strip())
title = po_pretty.find('span',attrs={'id':'productTitle'})
print(title.text.strip())


#usedPrice