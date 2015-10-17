import bs4, requests

def getAmazonPrice(productUrl):
    res =requests.get(productUrl)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#comp-pattern-library > div > div > a.title-link > h3 > span')
    return elems[0].text.strip()
    
price=getAmazonPrice('http://www.bbc.com/news')
print('The news is '+price)
