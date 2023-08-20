import pandas as pd 
import requests
from bs4 import BeautifulSoup
from filters import flipkart_url

r = requests.get(flipkart_url)

print(r)