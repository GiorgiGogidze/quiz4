import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

f = open('myauto.csv', 'w', newline='\n')
# f.write('Title,Year,Ranking\n')
file_obj = csv.writer(f)
file_obj.writerow(['Title', 'Year', 'Ranking'])

ind = 1
while ind < 125:
    url = 'https://www.myauto.ge/ka/s/0/0/00/00/00/00/00/00/iyideba-avtomobilebi?stype=0&for_rent=0&currency_id=3&det_search=0&ord=7&keyword=&category_id=m0&page='+str(ind)
    r = requests.get(url, headers=h)
    content = r.text

    soup = BeautifulSoup(content, 'html.parcer')
    all_cars_block = soup.find('div', class_='search-lists-container')
    all_cars = all_cars_block.find_all('div', class_='current-item')

    for each in all_cars:
        title = each.h4.a.text
        print(title)
        year = each.find('p', class_='car-levy').text
        print(year)
        price = each.find('div', class_='new-price-container').text
        print(price)
        # f.write(title+','+year+','+rating+'\n')
        file_obj.writerow([title, year, rating])
    ind +=25
    sleep(randint(15,20))
