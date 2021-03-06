{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "74198649",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import requests\n",
    "import pprint\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0a26600d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 102.0.5005\n",
      "Get LATEST chromedriver version for 102.0.5005 google-chrome\n",
      "Driver [/Users/heyleenah/.wdm/drivers/chromedriver/mac64/102.0.5005.61/chromedriver] found in cache\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6081140f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's Ingenuity Mars Helicopter Captures Video of Record Flight\n",
      "Imagery has come down from Mars capturing a recent flight in which the rotorcraft flew farther and faster than ever before. \n"
     ]
    }
   ],
   "source": [
    "#Navigate to url for scraping\n",
    "news_url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(news_url)\n",
    "\n",
    "\n",
    "#Get browser html into object for scraping\n",
    "news_html = browser.html\n",
    "\n",
    "#Parse with beautiful soup parser\n",
    "soup = BeautifulSoup(news_html, \"html.parser\")\n",
    "\n",
    "#Scrape the Mars News Site and collect the latest News Title and Paragraph Text\n",
    "#Assign the text to variables that you can reference later.\n",
    "results = soup.find('div' , class_ = \"list_text\")\n",
    "\n",
    "news_title = results.a.text\n",
    "news_p = results.find(\"div\" , class_ = \"article_teaser_body\").text\n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bde1ee84",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://mars.nasa.gov/news/image/featured/mars3.jpg'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jpl_url = 'https://spaceimages-mars.com'\n",
    "browser.visit(jpl_url)\n",
    "\n",
    "jpl_html = browser.html\n",
    "soup = BeautifulSoup(jpl_html, 'html.parser')\n",
    "\n",
    "img = soup.find('img', class_ = 'headerimage fade-in')\n",
    "img_url = url + img['src']\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5c9950c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                         0                1                2\n",
       " 0  Mars - Earth Comparison             Mars            Earth\n",
       " 1                Diameter:         6,779 km        12,742 km\n",
       " 2                    Mass:  6.39 ?? 10^23 kg  5.97 ?? 10^24 kg\n",
       " 3                   Moons:                2                1\n",
       " 4       Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 5          Length of Year:   687 Earth days      365.24 days\n",
       " 6             Temperature:     -87 to -5 ??C      -88 to 58??C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 ?? 10^23 kg (0.11 Earths)\n",
       " 3                Moons:          2 ( Phobos & Deimos )\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 ??C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fact_url = 'https://galaxyfacts-mars.com'\n",
    "browser.visit(fact_url)\n",
    "\n",
    "mars_fact = pd.read_html(fact_url)\n",
    "\n",
    "type(mars_fact)\n",
    "\n",
    "mars_fact"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "817cd324",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'title': 'Cerberus Hemisphere Enhanced', 'image url': 'https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'image url': 'https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'image url': 'https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'image url': 'https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}]\n"
     ]
    }
   ],
   "source": [
    "#To hold  our loop iterations\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "for x in range (4):\n",
    "    hemi_url  = \"https://marshemispheres.com/\"\n",
    "    browser.visit(hemi_url)\n",
    "    image = browser.find_by_tag('h3')\n",
    "    time.sleep(5)\n",
    "    image[x].click()\n",
    "    html1 = browser.html\n",
    "    soup = BeautifulSoup(html1, 'html.parser')\n",
    "    url1 = soup.find('img', class_='wide-image')['src']\n",
    "    title = soup.find('h2', class_ = 'title').text\n",
    "\n",
    "    dict = {'title': title, 'image url': hemi_url + url1}\n",
    "    hemisphere_image_urls.append(dict)\n",
    "\n",
    "print(hemisphere_image_urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "93322a0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "955919ee",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
