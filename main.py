import requests

url = "https://search.naver.com/search.naver?where=nexearch&query=오늘의 일본어"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

idx = html.find("男性")

print("index =", idx)

print(html[idx-500:idx+500])

raise Exception("주변 확인")
