#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import pprint
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


#Navigate to url for scraping
news_url = 'https://mars.nasa.gov/news/'
browser.visit(news_url)


#Get browser html into object for scraping
news_html = browser.html

#Parse with beautiful soup parser
soup = BeautifulSoup(news_html, "html.parser")

#Scrape the Mars News Site and collect the latest News Title and Paragraph Text
#Assign the text to variables that you can reference later.
results = soup.find('div' , class_ = "list_text")

news_title = results.a.text
news_p = results.find("div" , class_ = "article_teaser_body").text
print(news_title)
print(news_p)


# In[5]:


jpl_url = 'https://spaceimages-mars.com'
browser.visit(jpl_url)

jpl_html = browser.html
soup = BeautifulSoup(jpl_html, 'html.parser')

img = soup.find('img', class_ = 'headerimage fade-in')
img_url = url + img['src']
img_url


# In[6]:


fact_url = 'https://galaxyfacts-mars.com'
browser.visit(fact_url)

mars_fact = pd.read_html(fact_url)

type(mars_fact)

mars_fact


# In[8]:


#To hold  our loop iterations
hemisphere_image_urls = []

for x in range (4):
    hemi_url  = "https://marshemispheres.com/"
    browser.visit(hemi_url)
    image = browser.find_by_tag('h3')
    time.sleep(5)
    image[x].click()
    html1 = browser.html
    soup = BeautifulSoup(html1, 'html.parser')
    url1 = soup.find('img', class_='wide-image')['src']
    title = soup.find('h2', class_ = 'title').text

    dict = {'title': title, 'image url': hemi_url + url1}
    hemisphere_image_urls.append(dict)

print(hemisphere_image_urls)


# In[9]:


browser.quit()


# In[ ]:




