import requests

url = "https://search.naver.com/search.naver?where=nexearch&query=오늘의 일본어"

html_text = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

print("길이 =", len(html_text))

for keyword in [
    "list_html",
    "word_item",
    "오늘의 일본어",
    "_sap_item",
    "page_link"
]:
    print(keyword, "=>", keyword in html_text)

print(html_text[:3000])

raise Exception("확인")
