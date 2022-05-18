from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# URLto Scrape Data
bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

# Get Page
page = requests.get(bright_stars_url)
print(page)

# Parse Page
soup = bs(page.text,'html.parser')

star_table = soup.find('table')

temp_list= []
stars = []
distance =[]
mass = []
radies =[]
bri = []

table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1,len(temp_list)):
    stars.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radies.append(temp_list[i][6])
    bri.append(temp_list[i][7])

top = ['star','distance','mass','radies','britness']    
df2 = pd.DataFrame(list(zip(stars,distance,mass,radies,bri)),columns=top)
print(df2)

df2.to_csv('bright_stars.csv', index=True, index_label="id")