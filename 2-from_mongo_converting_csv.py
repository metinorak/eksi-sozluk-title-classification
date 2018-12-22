from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.eksidm
col = db.titleandcategories


all_data = col.find()



file = open('data.csv', 'w')


categories = ['spor',
              'ilişkiler',
              'siyaset',
              'seyahat',
              'otomotiv',
              'tv',
              'anket',
              'bilim',
              'edebiyat',
              'eğitim', 
              'ekonomi',
              'ekşi-sözlük',
              'haber',
              'havacılık',
              'magazin',
              'moda',
              'motosiklet',
              'müzik',
              'oyun',
              'programlama',
              'sağlık',
              'sanat',
              'sinema',
              'spoiler',
              'tarih',
              'teknoloji',
              'yeme-içme'
              ]
line = 'title,'
for cat in categories:
  line += (cat + ',')
line = line.strip(',')

file.write(line + '\n')



for item in all_data:

  line_to_add = ""
  line_to_add += item['title'] + ','
  cats = item['categories']

  for cat in categories:
    if cat in cats:
      line_to_add += '1,'
    else:
      line_to_add += '0,'
  
  line_to_add = line_to_add.strip(',')
  file.write(line_to_add + '\n')

client.close()
file.close()

