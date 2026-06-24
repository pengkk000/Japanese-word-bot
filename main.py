import requests
import re
import html
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&query=오늘의 일본어"

html_text = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

m = re.search(r'"list_html":"(.*?)","page_link"', html_text)

if not m:
    raise Exception("list_html 못 찾음")

list_html = html.unescape(
    m.group(1)
        .replace('\\"', '"')
        .replace("\\/", "/")
)

soup = BeautifulSoup(list_html, "html.parser")

for item in soup.select("li.word_item_sap_item"):
    print("-----")
    print(item.get_text(" ", strip=True))
