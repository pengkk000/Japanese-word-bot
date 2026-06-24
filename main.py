import requests

url = "https://search.naver.com/search.naver?where=nexearch&query=오늘의 일본어"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

idx = html.find("だんせい")

print("idx =", idx)

print(html[idx-1500:idx+3000])

raise Exception("주변 확인")
