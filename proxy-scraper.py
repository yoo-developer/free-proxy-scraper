from bs4 import BeautifulSoup
import requests
proxies = []
proxysite = requests.get("https://free-proxy-list.net/")

soup = BeautifulSoup(proxysite.content, 'html.parser')
i = 0
proxy = [0]
while i <= len(soup.select('td')) :
        if i%8 == 1 :
                p0 = soup.select('td')[i-1].text
                print(p0)
                proxies.append(p0)
        i += 1

print(proxy)
