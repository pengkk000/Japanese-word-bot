import requests

url = "https://search.naver.com/search.naver?where=nexearch&query=오늘의 일본어"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(url, headers=headers).text

print(html[:10000])

raise Exception("확인")
