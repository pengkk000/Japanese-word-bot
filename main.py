import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&query=오늘의 일본어"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

soup = BeautifulSoup(html, "html.parser")

words = soup.select("div.word")

print("개수:", len(words))

for w in words[:10]:
    print("-----")
    print(w.get_text(" ", strip=True))
