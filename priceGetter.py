import bs4
import requests

def getAmazonPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')   #soup object
    elems = soup.select('#priceblock_ourprice')         #elems becomes a list
    return elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.com/ROLAND-Electronic-Drum-Set-TD-11KV/dp/B00AKQVUSA/ref=sr_1_10?ie=UTF8&qid=1538523379&sr=8-10&keywords=drum+set')
print('The price is ' + price)



