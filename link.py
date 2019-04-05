# import requests
# from parsel import Selector

import requests
import urllib.request
from bs4 import BeautifulSoup

def get_html():
    url = 'https://dmv.vermont.gov/registrations/new'
    response = requests.get(url)

    return response
    
	
if __name__ == "__main__":
    response = get_html()
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all('a')
    
    for link in links:
        print(link.get('href'))
   

