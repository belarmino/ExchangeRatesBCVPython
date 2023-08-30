from bs4 import BeautifulSoup
import requests
request = requests.get('https://www.bcv.cv/en/Pages/Homepage.aspx')

processPage = BeautifulSoup(request.text)
lines = processPage.select('.rate-exchange__row')
i = 1
CountryCode = ""
CountryName = ""
Purchase = ""
PurchaseMobile = ""
listExchange = []
for line in lines:
    if i > 2:
        CountryCode = line.find('p', class_='rate-exchange__row-c1-code').text
        CountryName = line.find(
            'p', class_='rate-exchange__row-c1-country').text
        Purchase = line.find('td', class_='rate-exchange__row-c2').text
        PurchaseMobile = line.find('td', class_='rate-exchange__row-c2').find('span',
                                                                              'rate-exchange__row-mobile').text
        Sale = line.find('td', class_='rate-exchange__row-c3').text

        print('------------------------------------------------')

        Purchase = Purchase[:-len(PurchaseMobile)]

        print(CountryCode)
        print(CountryName)
        print(PurchaseMobile)
        print(Purchase)
        print(Sale)
        print('------------------------------------------------')
    i = i+1
