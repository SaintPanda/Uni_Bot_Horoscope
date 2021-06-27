#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import re
import emoji
import pendulum as pdl
import json

time = pdl.now("Europe/London")


# In[4]:


url = "https://lifestyle.segodnya.ua/lifestyle/psychology.html"
HEADERS = {

    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}


# In[5]:


# Загрузка основной страницы
if dt !=time.day :
    response = requests.get(url, headers = HEADERS)
    
    src = response.text
    
    with open("data_day/Life_index.html", "w",errors='ignore') as file:
        file.write(src)  
    with open("data_day/Life_index.html") as file:
        srss = file.read()
        
    soup = BeautifulSoup(srss,'html.parser')

    iteams_href_main = soup.findAll(href = re.compile(f"goroskop-na-segodnya-{time.day}"))

    main = [i.get("href") for i in iteams_href_main][0]
    
    with open("data_day/Life_index_clear.json", "w",errors='ignore') as file:
        json.dump(main, file, indent=4, ensure_ascii=False)  
        
    


# In[10]:


with open("data_day/Life_index_clear.json", errors='ignore') as file:
    working_href = json.load(file)
    
comp_title = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']    
req = requests.get(working_href, headers = HEADERS)
srs = req.text

soup = BeautifulSoup(srs,'html.parser')
_1st_block = soup.find_all("p")

hor = [i.text for i in _1st_block]
del hor[:5]
comps_text_clear = hor[::3]


# In[ ]:




