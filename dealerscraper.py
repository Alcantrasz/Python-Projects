#Call BeatifulSoup library
from bs4 import BeautifulSoup
#Call Request Module 
import requests, openpyxl

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Car Dealership Bot'
print(excel.sheetnames)
sheet.append(['Car Model','Car Price','Car Price Rating','Car Distance','Car Delivery Range'])

try:
    for x in range(1, 50):
        source = requests.get(f'https://www.truecar.com/used-cars-for-sale/listings/location-lynn-ma/?page={x}')
        source.raise_for_status()

        soup = BeautifulSoup(source.text, 'html.parser')

        cars = soup.find('div', class_="md:pt-2").find_all('li', class_="mt-3 flex grow col-md-6 col-xl-4")
        
        for car in cars:
            
            model = car.find('div', class_="w-full truncate").div.text
            price = car.find('div', class_="mt-1 flex items-center justify-between").h3.span.text
            priceRating = car.find('div', class_="flex items-center ml-1").text
            range = car.find('div', class_="flex w-full justify-between").div.text
            delivery = car.find('div', class_="min-h-[18px]").text

            print(model, price, priceRating, range, delivery)
            sheet.append([model, price, priceRating, range, delivery])

except Exception as exc:
    print(exc)

excel.save('Car Dealership Bot.xlsx')