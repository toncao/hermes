import requests
from bs4 import BeautifulSoup

class scrap():

    def __init__(self, count = 5):
        self.count = count

    def vnexpress(self):
        url = 'https://vnexpress.net/'
        soup = BeautifulSoup(requests.get(url).content, 'html5lib').find_all('p', attrs = {'class': 'description'})
        news =[{'title': content.a['title'],
                'description': content.a.string,
                'link': content.a['href']} for content in soup[:min(self.count,len(soup))]]
        return news
