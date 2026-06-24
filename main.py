import requests

url = "https://wquiz.dict.naver.com/jakodict/today/quiz.dict"

html = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
).text

print(html[:5000])
