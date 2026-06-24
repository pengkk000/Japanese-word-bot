import requests
import re

url = "https://wquiz.dict.naver.com/jakodict/today/words.dict?targetDate=20260625"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

for keyword in [
    "gateway",
    "api",
    "today",
    "word",
    "quiz",
    "ajax"
]:
    print(f"\n===== {keyword} =====")

    for m in re.finditer(keyword, html, re.IGNORECASE):
        start = max(0, m.start() - 200)
        end = min(len(html), m.end() + 500)
        print(html[start:end])
        break

raise Exception("검색 완료")
