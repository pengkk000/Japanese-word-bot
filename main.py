import requests

url = "https://search.naver.com/search.naver?where=nexearch&query=오늘의 일본어"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

idx = html.find('<div class="word"')

print("idx =", idx)

if idx != -1:
    print(html[idx:idx+3000])

raise Exception("확인")
