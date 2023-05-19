import requests
from bs4 import BeautifulSoup

class scrap():

    def __init__(self, count = 20):
        self.count = count

    def vnexpress(self):
        url = 'https://vnexpress.net'
        soup = BeautifulSoup(requests.get(url).content, 'html5lib').find_all('p', attrs = {'class': 'description'})
        news =[{'title': content.a['title'],
                'description': content.a.string,
                'link': content.a['href']} for content in soup[:min(self.count,len(soup))]]
        return news

    def tuoitre(self):
        url = 'https://tuoitre.vn'
        soup = BeautifulSoup(requests.get(url).content, 'html5lib').find_all('a', attrs = {'class': 'box-category-link-title'})
        news =[{'title': content['title'],
                'description': None,
                'link': url + content['href']} for content in soup[:min(self.count,len(soup))]]
        return news

    def thanhnien(self):
        url = 'https://thanhnien.vn'
        soup = BeautifulSoup(requests.get(url).content, 'html5lib').find_all('a', attrs = {'class': 'box-category-link-title'})
        news =[{'title': content['title'],
                'description': None,
                'link': url + content['href']} for content in soup[3:min(self.count+3,len(soup))]]
        return news
