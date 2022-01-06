#!python3
import bs4
import requests
import re
#TODO make functions for various scraping desires
#https://www.geeksforgeeks.org/scraping-amazon-product-information-using-beautiful-soup/


def get_price(product_url):
        headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
        ro = requests.get(product_url,headers = headers)
        ro.raise_for_status()
        #print(ro.text)
        t = ro.text
        find_span = re.compile(r'<span\sid="(.*?)"')
        fo = find_span.findall(t)
        po = bs4.BeautifulSoup(ro.content,'html.parser')
        po_pretty = bs4.BeautifulSoup(po.prettify(),'html.parser')
        nf = open('amazon.csv','a')
        for i in fo:
            pr = po_pretty.find("span", attrs={'id': i})
            entry = (i+':'+pr.text.strip())
            nf.write(entry)
            nf.write('\n')
        nf.close()

                
                
                
            
        


print(get_price(r"https://www.amazon.com/Automate-Boring-Stuff-Python-2nd-dp-1593279922/dp/1593279922/ref=mt_other?_encoding=UTF8&me=&qid=1641447778"))