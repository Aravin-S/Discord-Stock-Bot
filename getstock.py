import requests 
from bs4 import BeautifulSoup

def getData(symbol):
    url = f'https://ca.finance.yahoo.com/quote/{symbol}'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
    'symbol' :symbol,
    'price': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
    'change': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
    'perc': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text,
   }
    return stock

