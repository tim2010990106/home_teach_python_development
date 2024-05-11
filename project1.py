import requests
from bs4 import BeautifulSoup
url = 'https://invoice.etax.nat.gov.tw/index.html'
web = requests.get(url)    
web.encoding='utf-8'       

soup = BeautifulSoup(web.text, "html.parser")                    
td = soup.select('.container-fluid')[0].select('.etw-tbiggest')  
ns = td[0].getText()  
n1 = td[1].getText()  

n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]] 

while 1:
    try:
        num = input('輸入你的發票號碼：')
        if num == ns: print('對中 1000 萬元！')
        if num == n1: print('對中 200 萬元！')
        for i in n2:
            if num == i:
                print('對中 20 萬元！')
                break
            if num[-7:] == i[-7:]:
                print('對中 4 萬元！')
                break
            if num[-6:] == i[-6:]:
                print('對中 1 萬元！')
                break
            if num[-5:] == i[-5:]:
                print('對中 4000 元！')
                break
            if num[-4:] == i[-4:]:
                print('對中 1000 元！')
                break
            if num[-3:] == i[-3:]:
                print('對中 200 元！')
                break
    except: break