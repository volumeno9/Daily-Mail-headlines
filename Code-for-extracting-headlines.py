from newsapi import NewsApiClient
import requests
import pandas as pd 
from pandas.io.json import json_normalize    


keywords = ['naked', 'hourglass'
'nude',
'waist',
'midriff',
'abs',
'ample assets',
'bust', 'busty',
'butt',
'cleavage',
'curves',
'derriere',
'figure',
'gams',
'leggy',
'legs',
'physique',
'toned',
'pins',
'skin ',
'flesh',
'thigh',
'plunging',
'braless',
'bikini',
'to the imagination',
'sexy',
'racy',
'revealing',
'swimsuit',
'lingerie',
'thong',
'underwear',
'skintight',
'frame',
'skin-tight',
'tummy',
'skimpy', 'strips', 'sultry', 'bra-less', 'sizzling', 'sizzles', 'g-string', 'takes the plunge', 'stomach']


# Init
newsapi = NewsApiClient(api_key='yourAPIhere')

for keyword in keywords:
    allkeywords = pd.DataFrame()
    url ="https://newsapi.org/v2/everything?domains=dailymail.co.uk&qInTitle=" + keyword + "&from=2019-11-01&to=2019-11-30&pageSize=100&language=en&apiKey=yourAPIhere"
    data = requests.get(url).json() 
    total = json_normalize(data['articles'])
    total.to_excel(('yourfolder' + keyword + '.xlsx'), index=False)
