import requests
import re

url = "https://wquiz.dict.naver.com/jakodict/today/words.dict"

html = requests.get(url).text

for line in html.split("\n"):
    if "api" in line.lower():
        print(line)

raise Exception("API 검색 완료")
