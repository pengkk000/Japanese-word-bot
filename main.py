import requests

url = "https://search.naver.com/search.naver?where=nexearch&query=오늘의 일본어"

html_text = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

print("list_html 존재:", "list_html" in html_text)

idx = html_text.find("list_html")

print("idx =", idx)

if idx != -1:
    print(html_text[idx:idx+3000])

raise Exception("확인")
