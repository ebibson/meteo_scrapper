import requests

r = requests.get("https://assets.msn.com/weathermapdata/1/static/svg/72/v2/card_fix_partlysunny/CloudyV3.sv")

print(r.text)
