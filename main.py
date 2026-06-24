import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&query=오늘의 일본어"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(url, headers=headers).text

soup = BeautifulSoup(html, "html.parser")

for text in soup.stripped_strings:
    if "男性" in text or "画家" in text:
        print(text)

raise Exception("확인")
