from bs4 import BeautifulSoup
import requests
from lxml import etree

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

url = 'https://www.zillow.com/profile/nicholasryanteam/'
source = requests.get(url, headers=headers).text
soup = BeautifulSoup(source, 'lxml')

company_name = soup.find('div', class_='Text-c11n-8-39-0__aiai24-0 hWdvTH')
print(company_name)

name = soup.find('div', class_='Text-c11n-8-39-0__aiai24-0 StyledHeading-c11n-8-39-0__ktujwe-0 gDqTKI')
print(name)
try:
  role = soup.find('div', class_='Text-c11n-8-39-0__aiai24-0 kaedsS').text
  print(role)
except:
  pass

sales = soup.find('p', class_='Text-c11n-8-39-0__aiai24-0 StyledParagraph-c11n-8-39-0__sc-18ze78a-0 jMsmDX').text
print(sales)

website = etree.HTML(str(soup))
print(website.xpath('//*[@id="__next"]/div/div[3]/aside/div[2]/div/dl/div[3]/dd/span/a[1]')[0].get('href'))
#website = soup.find('a', class_='StyledTextButton-c11n-8-39-0__n1gfmh-0 hKdCXh').text
#print(website)

facebook = etree.HTML(str(soup))
print(facebook.xpath('//*[@id="__next"]/div/div[3]/aside/div[2]/div/dl/div[3]/dd/span/a[3]')[0].get('href'))

linkedin = etree.HTML(str(soup))
print(linkedin.xpath('//*[@id="__next"]/div/div[3]/aside/div[2]/div/dl/div[3]/dd/span/a[5]')[0].get('href'))

#nicholasryanrealestate@gmail.com