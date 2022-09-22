import requests
import bs4
from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'год']

if __name__ == '__main__':
 base_url = 'https://habr.com/'
 url = base_url + 'ru/all' 
 header = Headers (browser = 'chrome', os = 'win', headers = True).generate()
 resp = requests.get (url, headers = header)
 text_page = resp.text
 
 soup1 = bs4.BeautifulSoup (text_page, features='html.parser')
 
 articles = soup1.find_all ('article')
 
 for artic in articles:
   hubs = artic.find_all(class_="tm-article-snippet__hubs")
   hubs = [hub.text.strip() for hub in hubs]
   if hubs in KEYWORDS:
    print (hubs)
    print()
 
 