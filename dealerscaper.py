#Call BeatifulSoup library
from bs4 import BeautifulSoup
#Call Request Module 
import requests

baseurl = 'https://www.truecar.com/'

carlinks = []

for x in range(1, 3):
  r = requests.get(f'https://www.truecar.com/used-cars-for-sale/listings/location-lynn-ma/?page={x}')
  soup = BeautifulSoup(r.content, 'html.parser')
  
  carlist = soup.find_all('li', class_='mt-3 flex grow col-md-6 col-xl-4')
  s = 'mt-3 flex grow col-md-6 col-xl-4'

  for s in carlist:
    for link in s.find_all('a', href=True):
      carlinks.append(baseurl + link['href'])


testlink = 'https://www.truecar.com/used-cars-for-sale/listing/2HKRW2H53MH669955/2021-honda-cr-v/?position=3&sourceType=marketplace'

r = requests.get(testlink)

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.find('div', class_='heading-3_5 normal-case heading-md-2 md:normal-case grow leading-[1.2] mb-1'))








    #for allVehicleListings in carlist:
     #   for link in allVehicleListings.find_all("a", href=True):
      #      print(link["href"])
    
    
    
    #make = soup.find("div", class_="w-full truncate font-bold").text.strip()
    #model = soup.find("div", class_="text-sm").text.strip()
    #price = soup.find("span", class_="truncate").text.strip()

    #print(make)
    #print(model)
    #print(price)