import requests

url = "https://search.naver.com/search.naver?where=nexearch&query=오늘의 일본어"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(url, headers=headers).text

keywords = [
    "오늘의 일본어",
    "だんせい",
    "男性",
    "がか",
    "画家"
]

for k in keywords:
    print(k, "=>", k in html)

raise Exception("검색 확인")
