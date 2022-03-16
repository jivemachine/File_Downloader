# Imports
from bs4 import BeautifulSoup
import requests
from requests import get

# get URL
page = requests.get(input('Enter URL: ')) # get URL
filetype = '.' + input('Enter File Extension (with no dot): ') # get file extension
soup = BeautifulSoup(page.text, 'html.parser') # parse the site using bs4

for link in soup.find_all('a'):
    url = link.get('href')
    if filetype in url:
        print(url)
        with open(url, 'wb') as file:
            response = get(url)
            file.write(response.content)
    else:
        continue