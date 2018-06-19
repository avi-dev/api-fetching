import requests
import bs4 as bs
from pprint import pprint

# res = requests.get('https://en.wikipedia.org/wiki/Deep_learning')
res = requests.get('https://jsonplaceholder.typicode.com/comments')

with open('a.txt','w') as f:
    f.write(res.text)