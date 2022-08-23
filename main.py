import requests 
import bs4
from pprint import pprint


def main():
    site = requests.get("https://www.msn.com/fr-fr/meteo").text
    soup = bs4.BeautifulSoup(site, 'html.parser')

    someLinks = soup.find_all('a', class_="summaryTemperatureCompact-E1_1")

    for link in someLinks:
        print(link.text)
    
if __name__ == "__main__":
    main()
