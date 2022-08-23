import requests 
import bs4
from pprint import pprint


def main():
    site = requests.get("https://www.msn.com/fr-fr/meteo").text
    soup = bs4.BeautifulSoup(site, 'html.parser')

    someLinks = soup.find_all('a', class_="summaryTemperatureCompact-E1_1")
    advice = soup.find_all('div', class_="summaryCaptionCompact-E1_1")
    TOWN = soup.find_all('a', class_="location_name_main_container-E1_1")
    summary = soup.find_all('p', class_="summaryDescCompact-E1_1")
    date = soup.find_all('div', class_="labelUpdatetime-E1_1")
    
    for dt in date:
        print(dt.text)

    for link in someLinks:
        print(link.text)

    for town in TOWN:
        print(town.text)

    for summaries in summary:
        print(summaries.text)

    for something in advice:
        print(something.text)

if __name__ == "__main__":
    main()
