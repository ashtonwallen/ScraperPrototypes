import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def get_html():
    url = 'https://dmv.vermont.gov/registrations/new'
    response = requests.get(url)

    return response


if __name__ == "__main__":
    response = get_html()
    soup = BeautifulSoup(response.text, "html.parser")

    allFile =  open("AllContent.txt", "w")
    allFile.write(soup.text)
    allFile.close();


