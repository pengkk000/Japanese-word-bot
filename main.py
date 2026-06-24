import requests
import re

url = "https://wquiz.dict.naver.com/jakodict/today/words.dict?targetDate=20260625"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

matches = sorted(set(re.findall(r'[\w/\-]+\.dict(?:\?[^"\']*)?', html)))

print("찾은 .dict URL 후보들:")
print("=" * 50)

for m in matches:
    print(m)

print("=" * 50)
print("개수:", len(matches))
