# pip install requests
# pip install bs4

import requests
from bs4 import BeautifulSoup

# top 10 expensive cars url
url = 'https://www.boxymo.ie/news/most-expensive-cars-in-the-world.aspx'

# get data from the web
r = requests.get(url)

# specify the parser
soup = BeautifulSoup(r.content,'html.parser')

# get all the data with tags as 'p' and the class as 'panel-title-boxymo-black device-font'
price = soup.findAll('p',class_='panel-title-boxymo-black device-font')

# get text from each entry
price1 = [pt.get_text() for pt in price]

# sort the records
sorted_price = sorted(price1,key=lambda x : int(x.split('.')[0]))

# print the sorted list
for x in sorted_price:
    print(x)