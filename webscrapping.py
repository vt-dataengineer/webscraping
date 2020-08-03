import requests
from bs4 import BeautifulSoup
url = 'https://www.boxymo.ie/news/most-expensive-cars-in-the-world.aspx'

r = requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')


price = soup.findAll('p',class_='panel-title-boxymo-black device-font')

price1 = [pt.get_text() for pt in price]


    # print(x.split('.')[0])
sorted_price = sorted(price1,key=lambda x : int(x.split('.')[0]))
for x in sorted_price:
    print(x)