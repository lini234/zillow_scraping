from bs4 import BeautifulSoup
import requests, csv
import pandas as pd
from lxml import etree

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}


agentlist = []
fields = ['Name', 'Link']

city = 'austin-tx'
url = f'https://www.zillow.com/professionals/real-estate-agent-reviews/{city}/'
source = requests.get(url, headers=headers).text
soup = BeautifulSoup(source, 'lxml')

for agents in soup.find_all('div', class_='Flex-c11n-8-50-1__sc-n94bjd-0 cRqPtx'):
    name = agents.find('a', class_='StyledTextButton-c11n-8-50-1__sc-n1gfmh-0 efodvH').text
    print(name)
    profile_link = agents.find('a', class_ = 'StyledTextButton-c11n-8-50-1__sc-n1gfmh-0 efodvH').get('href')
    link = f'https://www.zillow.com{profile_link}'
    print(link)
    url2 = link
    source2 = requests.get(url2, headers=headers).text
    soup2 = BeautifulSoup(source2, 'lxml')

    #company_name = soup2.find('div', class_='Text-c11n-8-39-0__aiai24-0 hWdvTH').text
    #print(company_name)
    try:
        role = soup2.find('div', class_='Text-c11n-8-39-0__aiai24-0 kaedsS').text
    except:
        pass
    sales = soup2.find('p',
                               class_='Text-c11n-8-39-0__aiai24-0 StyledParagraph-c11n-8-39-0__sc-18ze78a-0 jMsmDX').text
    print(sales)
    try:
        website = etree.HTML(str(soup2))
        #print(website.xpath('//*[@id="__next"]/div/div[3]/aside/div[2]/div/dl/div[3]/dd/span/a[1]')[0].get('href'))
        web = website.xpath('//*[@id="__next"]/div/div[3]/aside/div[2]/div/dl/div[3]/dd/span/a[1]')[0].get('href')
        print(web)
    except:
        pass
    try:
        facebook = etree.HTML(str(soup2))
        #print(facebook.xpath('//*[@id="__next"]/div/div[3]/aside/div[2]/div/dl/div[3]/dd/span/a[3]')[0].get('href'))
        fb = facebook.xpath('//*[@id="__next"]/div/div[3]/aside/div[2]/div/dl/div[3]/dd/span/a[3]')[0].get('href')
        print(fb)
    except:
        pass
    try:
        linkedin = etree.HTML(str(soup2))
        #print(linkedin.xpath('//*[@id="__next"]/div/div[3]/aside/div[2]/div/dl/div[3]/dd/span/a[5]')[0].get('href'))
        linkdin = linkedin.xpath('//*[@id="__next"]/div/div[3]/aside/div[2]/div/dl/div[3]/dd/span/a[5]')[0].get('href')
        print(linkdin)
    except:
        pass

    print()


