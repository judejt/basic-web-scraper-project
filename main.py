# Importing Libraries 
import requests
import json 
import re
from bs4 import BeautifulSoup 
import csv 
from io import StringIO

# url 
url_anaylsis = 'https://finance.yahoo.com/quote/{}/analysis?p={}'
url_profile = 'https://finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://finance.yahoo.com/quote/{}/financials?p={}'

# Ticker
stock = 'F'

# Pulling Json 
response = requests.get(url_financials.format(stock, stock))
tastysoup =BeautifulSoup(response.text,'html.parser')

# Motif 
pattern = re.compile(r'\s--\sData\s--s\s')
script_data = tastysoup.find('script', text=pattern).contents[0]
start = script_data.find("context")-2
json_data = json.loads(script_data[start:-12])
json_data ['context'].keys()
#dict_keys(['dispatcher', 'options', 'plugins'])
json_data['context']['dispatcher']['stores'] ['QuoteSummaryStore']

# historical stock data
historical_stock_url = 'https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1639407638&period2=1670943638&interval=1d&events=history&includeAdjustedClose=true'
repsonse = requests.get(historical_stock_url)
response.text