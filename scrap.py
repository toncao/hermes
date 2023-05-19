import requests
from bs4 import BeautifulSoup
import json
import datetime

class scrap():

    def __init__(self, count = 20, export = False):
        self.count = count
        self.export = export

    def all(self):
        return self.vnexpress() + self.tuoitre() + self.thanhnien() + self.dantri()

    def vnexpress(self):
        url = 'https://vnexpress.net'
        soup = BeautifulSoup(requests.get(url).content, 'html5lib').find_all('p', attrs = {'class': 'description'})
        news =[{'title': content.a['title'],
                'description': content.a.text,
                'link': content.a['href']} for content in soup[2:min(self.count,len(soup))]]

        news = [{'title': soup[0].a['title'], 'description': soup[0].a.text + soup[1].a.text, 'link': soup[0].a['href']}] + news

        if self.export:
            file_name = 'vnexpress_' + datetime.datetime.now().isoformat(timespec = 'hours') + '.json'
            with open(file_name, 'w') as f:
                json.dump(news, f, indent = 4, ensure_ascii = False)

        return news

    def tuoitre(self):
        url = 'https://tuoitre.vn'
        soup = BeautifulSoup(requests.get(url).content, 'html5lib').find_all('a', attrs = {'class': 'box-category-link-title'})
        news =[{'title': content['title'],
                'description': None,
                'link': url + content['href']} for content in soup[:min(self.count,len(soup))]]

        if self.export:
             file_name = 'tuoitre_' + datetime.datetime.now().isoformat(timespec = 'hours') + '.json'
             with open(file_name, 'w') as f:
                 json.dump(news, f, indent = 4, ensure_ascii = False)

        return news

    def thanhnien(self):
        url = 'https://thanhnien.vn'
        soup = BeautifulSoup(requests.get(url).content, 'html5lib').find_all('a', attrs = {'class': 'box-category-link-title'})
        news =[{'title': content['title'],
                'description': None,
                'link': url + content['href']} for content in soup[3:min(self.count+3,len(soup))]]

        if self.export:
             file_name = 'thanhnien_' + datetime.datetime.now().isoformat(timespec = 'hours') + '.json'
             with open(file_name, 'w') as f:
                 json.dump(news, f, indent = 4, ensure_ascii = False)

        return news

    def dantri(self):
        url = 'https://dantri.com.vn/'
        soup = BeautifulSoup(requests.get(url).content, 'html5lib').find_all('h3', attrs = {'class': 'article-title'})
        news =[{'title': content.a.string,
                'description': None,
                'link': url + content.a['href']} for content in soup[:min(self.count,len(soup))]]

        if self.export:
             file_name = 'dantri_' + datetime.datetime.now().isoformat(timespec = 'hours') + '.json'
             with open(file_name, 'w') as f:
                 json.dump(news, f, indent = 4, ensure_ascii = False)

        return news
