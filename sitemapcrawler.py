import requests
from bs4 import BeautifulSoup

myURL = my-website-goes-here.com/sitemap.xml
page = requests.get(myURL)
soup = BeautifulSoup(page.content, 'html.parser')
urls = soup.find_all('loc')

for url in urls:
    currentURL = url.get_text()
    if ('.pdf' not in currentURL):
        page = requests.get(currentURL)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find('title')
        print(title.get_text())
