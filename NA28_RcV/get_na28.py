import requests
from bs4 import BeautifulSoup

url = "https://www.academic-bible.com/en/online-bibles/novum-testamentum-graece-na-28/read-the-bible-text/"
r = requests.get(url)
print(r.status_code)

html_content = r.text
soup = BeautifulSoup(html_content, 'html.parser')