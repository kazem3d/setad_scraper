import requests
from bs4 import BeautifulSoup
import csv


pages = []

for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/ano' + str(i) + '.htm'
    pages.append(url)


f = csv.writer(open('o-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')


    # Remove bottom links
    last_links = soup.find(class_='AlphaNav')

    last_links.decompose()


    # Pull all text from the BodyText div
    artist_name_list = soup.find(class_='BodyText')


    # Pull text from all instances of <a> tag within BodyText div
    artist_name_list_items = artist_name_list.find_all('a')


    print('***************')
    print(item)
    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')
        print(links)
        print(names)
        f.writerow([names, links])


