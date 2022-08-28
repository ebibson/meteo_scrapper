import requests 
import bs4


site = requests.get("https://www.msn.com/fr-fr/meteo").text
soup = bs4.BeautifulSoup(site, 'html.parser')

advice = soup.find_all('div', class_="summaryCaptionCompact-E1_1")
TOWN = soup.find_all('a', class_="location_name_main_container-E1_1")
someLinks = soup.find_all('a', class_="summaryTemperatureCompact-E1_1")
summary = soup.find_all('p', class_="summaryDescCompact-E1_1")
date = soup.find_all('div', class_="labelUpdatetime-E1_1")

def main():

    meteo = open("meteo.txt", "w")
    for dt in date:
        print(dt.text)
        meteo.write(dt.text)

    for link in someLinks:
        print(link.text)
        texting = str(link.text).split("\u200e")[0]
        print(texting)
        meteo.write(f"\n{texting} Celsius")

    for town in TOWN:
        print(town.text)
        meteo.write(f'\n{town.text}')

    for summaries in summary:
        print(summaries.text)
        meteo.write('\n' + summaries.text)

    for something in advice:
        print(something.text)
        meteo.write('\n' + something.text)

def for_test():
    global TOWN, summary, advice

    assert TOWN is True
    assert summary is True
    assert advice is True

if __name__ == "__main__":
    main()
