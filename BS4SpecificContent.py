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

    headers = soup.find_all('h3')

# doesnt totally work yet, currently get UL tags too early
# trying to figure out a way to not do the UL check if there is nothing following the <p> tag
    for tag in headers:
        print(tag.text)
        pTags = tag.find_next("p")

        for tagP in pTags:
            print("\t" + tagP)
            ulTags = tagP.find_next("ul")
            print(ulTags.text)




