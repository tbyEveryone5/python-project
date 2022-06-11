from bs4 import BeautifulSoup
import requests

url = 'https://www.showstart.com/event/166693'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
print(soup.prettify())