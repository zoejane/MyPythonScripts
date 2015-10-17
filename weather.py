import bs4, requests

def weatherurl(weatherUrl):
    res =requests.get(weatherUrl)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#feature-history > table > tbody > tr.hi > td:nth-child(5)')
    return elems[0].text.strip()
    
weather=weatherurl('http://www.accuweather.com/zh/cn/zhuzhou/59425/daily-weather-forecast/59425')
print('The price is '+weather)
