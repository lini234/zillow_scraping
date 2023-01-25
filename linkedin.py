import requests
import re

site = requests.get('https://www.linkedin.com/in/realtordamon')

agent = {
    'name': name,
    'link': link,
    'company': company_name,
    'sales': sales,
    'facebook': fb,
    'website': web,
    'linkedin': linkdin
}

agentlist.append(agent)

df = pd.DataFrame(agentlist)
print(df.head())
df.to_csv('agentlist.csv')

cities = ['dallas-tx', 'austin-tx', 'nashville-tn', 'boston-ma', 'seattle-wa']
for city in cities: