from bs4 import BeautifulSoup
import requests, lxml, csv
import pandas as pd

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}
page = 1
agentlist = []
while page != 5:
    page = page + 1
    city = 'dallas-tx'
    url = f'https://www.zillow.com/professionals/real-estate-agent-reviews/{city}/?page={page}'

    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'lxml')
    #print(soup.prettify())

    fields = ['Name', 'Link']

    for agents in soup.find_all('div', class_='Flex-c11n-8-50-1__sc-n94bjd-0 cRqPtx'):
        name = agents.find('a', class_='StyledTextButton-c11n-8-50-1__sc-n1gfmh-0 efodvH').text

        profile_link = agents.find('a', class_ = 'StyledTextButton-c11n-8-50-1__sc-n1gfmh-0 efodvH').get('href')
        link = f'https://www.zillow.com{profile_link}'
        agent = {
        'name': name,
        'link': link
        }
        agentlist.append(agent)

#print(len(agentlist))
#print(agentlist)

df = pd.DataFrame(agentlist)
print(df.head())
df.to_csv('agentlist.csv')