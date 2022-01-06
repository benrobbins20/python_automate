#!python3
import bs4
import requests
#TODO make functions for various scraping desires


def get_price(product_url):
    try:
        headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
        ro = requests.get(product_url,headers = headers)
        po = bs4.BeautifulSoup(ro.content,'html.parser')
        po_pretty = bs4.BeautifulSoup(po.prettify(),'html.parser')
        pr = po_pretty.find("span", attrs={'id': 'newBuyBoxPrice'}).text.strip()
        return "Used price: {}".format(pr)
    except:
        ro.raise_for_status()


print(get_price("https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994"))