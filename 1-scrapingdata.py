from bs4 import BeautifulSoup
import requests
#Pull the urls from sitemap.xml


page = requests.get(url = 'https://eksisozluk.com/sitemap.xml',  headers={"User-Agent":"Mozilla/5.0"}).text


soup = BeautifulSoup(page)

url_list = soup.find_all('loc')


urls = []

for item in url_list:
  urls.append(item.text)


#put the data to the mongodb


from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.eksidm
col = db.titleandcategories

def insert(data):
  if(not col.find({'title' : data['title']}).count()):
    col.insert_one(data)

#Find categories of urls
count = 1
for URL in urls:

  page = requests.get(url = URL,  headers={"User-Agent":"Mozilla/5.0"}).text

  soup = BeautifulSoup(page)

  title = BeautifulSoup(str(soup.find('title'))).text.split('-')[0].strip()
    
  cats = BeautifulSoup(str(soup.find(id = 'hidden-channels'))).text.strip()

  if(cats != 'None' and len(cats) != 0):
    cats = cats.split(',')
    data = {'title' : title, 'categories' : cats}
    insert(data)
    print(count)
    count += 1
    print("total record in mongo: ", col.count())
  


client.close()
