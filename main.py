import requests

url = "https://wquiz.dict.naver.com/jakodict/today/words.dict"

html = requests.get(url).text

for keyword in [
    "list_html",
    "word_item",
    "date_label",
    "todayWord",
    "quizData",
    "calendarData",
]:
    print("=" * 30)
    print(keyword)
    print(keyword in html)

raise Exception("검색 완료")
