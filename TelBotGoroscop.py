#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import telebot as tb
from telebot import types

from bs4 import BeautifulSoup
import requests
import re
import emoji
import pendulum as pdl

import numpy.random as np

file = open("API.txt", "r")

API_KEY = file.read()


# In[2]:


bot = tb.TeleBot(API_KEY)
var = 5
dt = 25
time = pdl.now("Europe/London")
# coding: utf8


# In[3]:


#Кнопки с зодиаками

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я Юни. Я тут главный бычок - Муууу {} \nЯ вместе со своими сестрами, можем рассказать, как пройдет твой сегодняшний день ".format(emoji.emojize(":cow_face:")))
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
    
    oven = types.KeyboardButton(text = "Овен")
    telets = types.KeyboardButton(text = "Телец")
    bliznets = types.KeyboardButton(text = "Близнецы")
    Rak = types.KeyboardButton(text = "Рак")
    Lev = types.KeyboardButton(text = "Лев")
    deva = types.KeyboardButton(text = "Дева")
    vesa = types.KeyboardButton(text = "Весы")
    scorp = types.KeyboardButton(text = "Скорпион")
    strel = types.KeyboardButton(text = "Стрелец")
    koz = types.KeyboardButton(text = "Козерог") 
    vodoley = types.KeyboardButton(text = "Водолей")
    riba = types.KeyboardButton(text = "Рыбы")
    
    
    markup_reply.add(oven,telets,bliznets,Rak,Lev,deva,vesa,scorp,strel,koz,vodoley,riba)
    bot.send_message(message.chat.id, "Выбери, у кого мне спросить ", reply_markup = markup_reply)


# In[4]:


#Прийом сообщений и отдача гороскопа

@bot.message_handler(content_types = ["text"])
def answer(message):
    comp_title = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']    
    if message.text in comp_title:
        for text in comp_title:
            if text == message.text:
                var = comp_title.index(text)
                bot.send_message(message.chat.id, ch_p(var))
    else:
        bot.send_message(message.chat.id, "Такой сестры у меня нет ... Попробуй еще раз {}".format(emoji.emojize(":face_savoring_food:")))


# In[5]:


# Рандомайзер с выбором парсера

def ch_p(var):
    numb = np.randint(1,6)
    if numb == 1:     
        q = parser_lifestyle(var)        
    if numb == 2:        
        q = parser_belta(var)        
    if numb == 3:       
        q = parser_astroscope(var)        
    if numb == 4:        
        q = parser_elle(var)        
    if numb == 5:        
        q = parse_TSN(var)
        
    return q
   


# In[6]:


my_emoji = [":ram:",":cow_face:",":performing_arts:",":crab:",":lion:",":princess:",":balance_scale:",":scorpion:",":bow_and_arrow:",":goat:",":spiral_shell:",":tropical_fish:"]


# In[7]:


def parse_TSN(var):

    get_ipython().run_line_magic('run', '"Parcer_TSN.ipynb"')
    
    return ("""{0} {1} {0} \n\n{2} """).format(emoji.emojize(my_emoji[var]), comp_title[var], comps_text_clear[var])
    
parse_TSN(var)  


# In[8]:


def parser_astroscope(var):
    
    get_ipython().run_line_magic('run', '"Parser_Astroscope.ipynb"')
  
    return ("""{0} {1} {0} \n{2} """).format(emoji.emojize(my_emoji[var]), comp_title[var], comps_text_clear[var])

parser_astroscope(var)


# In[9]:


def parser_belta(var):
    
    get_ipython().run_line_magic('run', '"Parser_belta.ipynb"')

    return ("""{0} {1} {0} \n\n{2} """).format(emoji.emojize(my_emoji[var]), comp_title[var], comps_text_clear[var])

parser_belta(var)


# In[10]:


def parser_lifestyle(var):

    get_ipython().run_line_magic('run', '"Parser_lifestyle.ipynb"')

    return ("""{0} {1} {0} \n\n{2} """).format(emoji.emojize(my_emoji[var]), comp_title[var], comps_text_clear[var])

parser_lifestyle(var)


# In[11]:


def parser_elle(var):

    get_ipython().run_line_magic('run', '"Parser_elle.ipynb"')

    return ("""{0} {1} {0} \n\n{2} """).format(emoji.emojize(my_emoji[var]), comp_title[var], comps_text_clear[var])

parser_elle(var)


# In[12]:


dt = time.day


# In[ ]:


bot.polling()


# In[17]:


var = comp_title.index("Рыбы")
var

