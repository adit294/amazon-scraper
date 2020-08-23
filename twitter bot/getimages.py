import requests
from bs4 import BeautifulSoup as bs
import os

url= 'https://aditagarwal.com/articles'

page= requests.get(url)
soup = bs(page.text, 'html.parser')

image_tags = soup.findAll('img')
if not os.path.exists('articleimages'):
    os.makedirs('articleimages')

os.chdir('articleimages')  

x=0

for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status.code ==200:
            with open('imagee-' + str(x) + '.jpg', 'wb' ) as f:
                f.writ(requests.get(url).content)
                f.close()
                x +=1
    except:
        pass