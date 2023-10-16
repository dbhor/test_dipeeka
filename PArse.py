from bs4 import BeautifulSoup as bs
import pandas as pd
#pd.set_option('display.max_colwidth', 500)
import time
import requests
import random

page = requests.get("https://www.goodreads.com/quotes/")
print(page)
soup = bs(page.content, "lxml")
#print(soup)
#print(soup.find_all(class_='authorOrTitle'))

authors = [i.text for i in soup.find_all(class_='authorOrTitle')]
print(authors)


""" above python script is webscrapping from www.goodreads.com/quotes, i am scrapping authors list from this page. """