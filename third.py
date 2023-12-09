import requests 
from bs4 import BeautifulSoup 

class property:
  def __init__(self, name, circle_rate,dev_rate):
    self.name = name
    self.circle_rate = circle_rate
    self.dev_rate = dev_rate

pincode = input('Enter Pincode : ')
URL = "https://dmnortheast.delhi.gov.in/std-pin-codes/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
pin_code = soup.find_all('span', {'class': 'bt-content'})
name_of_place = [] ;
i = 0
while i < len(pin_code):
    if((i+1 < len(pin_code)) and (pin_code[i+1].text == pincode)):
        name_of_place.append(pin_code[i].text)
    i += 1

# Data from magic bricks
URL2 = "https://www.magicbricks.com/blog/circle-rates-in-delhi/118402.html"
r = requests.get(URL2)

soup = BeautifulSoup(r.content, 'html5lib')
tables = soup.find_all('table')[1]
rows = tables.find_all(lambda tag: tag.name=='td')

data = []
i = 0
while i < len(rows):
    if i > 4 and i % 5 == 0:
        for names in name_of_place:
            if (rows[i].text).strip().lower() in names.strip().lower():
                circle_cost = rows[i+2].text
                dev = rows[i+3].text
                p = property(names.strip().lower(),circle_cost,dev)
                data.append(p)
    i = i+1

# Data from housing.com
URL3 = "https://housing.com/news/new-delhi-circle-rate/"
r = requests.get(URL3)

soup = BeautifulSoup(r.content, 'html5lib')
tables2 = soup.find_all('table')[3]
rows2 = tables2.find_all(lambda tag: tag.name=='td')

data2 = []
i = 0;
while i < len(rows2):
    if i > 2 and i % 3 == 0:
        for names in name_of_place:
            if (rows2[i].text).strip().lower() in names.strip().lower():
                circle_cost = rows2[i+1].text
                dev = rows2[i+2].text
                p = property(names.strip().lower(),circle_cost,dev)
                data2.append(p)
    i = i+1

if len(data) > 0:
    print('Data from MagicBrick Website.')
    for cost in data:
        print('Name of Place : '+ cost.name)
        print('Circle Rate : '+ cost.circle_rate)
        print('Development Cost : '+ cost.dev_rate)
else:
    print('Data not preset right now on MagicBrick.')

if len(data2) > 0:
    print()
    print()
    print('Data from Housing Website.')
    for cost in data2:
        print('Name of Place : ' + cost.name)
        print('Circle Rate : ' + cost.circle_rate)
        print('Development Cost : ' + cost.dev_rate)
else:
    print('Data not preset right now on housing.com.')

