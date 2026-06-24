import requests

url = "https://wquiz.dict.naver.com/jakodict/today/words.dict?targetDate=20260625"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

print(html[:5000])

raise Exception("확인")
