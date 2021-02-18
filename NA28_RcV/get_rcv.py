import requests

url = "https://text.recoveryversion.bible/RcV.htm"
r = requests.get(url)
print(r.status_code)

html_content = r.text
soup = BeautifulSoup(html_content, 'html.parser')