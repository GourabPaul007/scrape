import requests
from bs4 import BeautifulSoup
import json

# url = 'https://www.cdkeys.com/pc'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# oldPrices = soup.select('span[data-price-type="oldPrice"] span')
# products = soup.select('li.product-item')
# for i in range(len(products)):
#    # convert the data in the html attributes to json 
#    prod = json.loads(products[i]['data-impression'])
#    # print the product info 
#    print(f"{prod['name']} - ${prod['price']} - {oldPrices[i].text}")

# url = 'https://indiankanoon.org/doc/31592793/'
# a = soup.select('div[id="div_1"] span[class="akn-p"]')

url = 'https://indiankanoon.org/browse/union-act/1074/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
a = soup.select('div[class="browselist"]')

print(a)
# products = soup.select('li.product-item')

# for i in range(len(products)):
#    # convert the data in the html attributes to json 
#    prod = json.loads(products[i]['data-impression'])

#    # print the product info 
#    print(f"{prod['name']} - ${prod['price']} - {oldPrices[i].text}")


# soup = BeautifulSoup(response.content, 'html.parser')
# x = soup.select('div[class="browselist"]')
# # # get all hrefs in the page('entire year' and all months)
# # hrefs = []
# # for a in soup.find_all('a', href=True):
# #     hrefs.append(a['href'])

# resultSetHrefs = []
# for href in hrefs:
#     # if '/search/' in href and 'fromdate:1-1' in href and 'todate: 31-12' in href:
#     if '/search/' in href and href.value == 'Entire Year':
#         print(href)
#         eachMonth = requests.get('https://indiankanoon.org' + href)
#         eachMonthSoup = BeautifulSoup(eachMonth.content, 'html.parser')
#         resultSet = eachMonthSoup.select('div[class="result"]')
        
#         if(len(resultSet) > 0):
#             for result in resultSet:
#                 a_href = result.find('a')['href']
#                 if a_href not in resultSetHrefs:
#                     resultSetHrefs.append(a_href)
# print(resultSetHrefs)


# for href in hrefs:
#     if '/doc/' in href:
#         print(href)
#         response = requests.get('https://indiankanoon.org' + href)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         x = soup.select('div[class="docwrapper"]')

