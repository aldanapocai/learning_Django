import requests
from bs4 import BeautifulSoup


res = requests.get("https://www.codewithtomi.com/")

#BeautifulSoup to render data

soup = BeautifulSoup(res.content, 'html.parser')

s = soup.find('p', class_='post-snippet')

print(s.text)

# s = soup.find_all('h2', class_='post-title')

# for data in s:
#     print(data.text)