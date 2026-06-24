import requests
import html
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&query=오늘의 일본어"

html_text = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

idx = html_text.find('"list_html":"')

if idx == -1:
    raise Exception("list_html 못 찾음")

start = idx + len('"list_html":"')
end = html_text.find('","page_link"', start)

list_html = html_text[start:end]

list_html = bytes(list_html, "utf-8").decode("unicode_escape")
list_html = html.unescape(list_html)

soup = BeautifulSoup(list_html, "html.parser")

items = soup.select("li.word_item")

print("개수:", len(items))

if len(items) == 0:
    print(list_html[:1000])

for item in items:
    print("================================")
    print(item.get_text(" ", strip=True))
