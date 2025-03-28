import requests
from bs4 import BeautifulSoup

def abc(sayfa_url, file):
    r = requests.get(sayfa_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    list = soup.find_all("div", {"class": "f-cat f-item"})

    for i in list:
        print('============================================')
        
        for b in i.findAll("ul", {"class": "list underline"}):
            for link in b.findAll('a'):
                my_link = link.get('href') + "\n"
                newlink="www.milligazete.com.tr" + my_link
                print(newlink)
                    
                file.write(my_link)

haberler = [
    "https://www.milligazete.com.tr/arsiv/2025-04-18",
    "https://www.milligazete.com.tr/arsiv/2025-04-19",
    "https://www.milligazete.com.tr/arsiv/2025-04-20",
    "https://www.milligazete.com.tr/arsiv/2025-04-21",
    "https://www.milligazete.com.tr/arsiv/2025-04-22",
]

with open('tuçe.txt', 'a', encoding="utf-8") as file:
    for sayfa_url in haberler:
        abc(sayfa_url, file)
