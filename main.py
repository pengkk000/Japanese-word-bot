import os
import re
import requests
from bs4 import BeautifulSoup
from notion_client import Client
from datetime import datetime

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["DATABASE_ID"]

notion = Client(auth=NOTION_TOKEN)

url = "https://wquiz.dict.naver.com/jakodict/today/words.dict"

html = requests.get(url).text

matches = re.findall(
    r'"date_label":\s*"([^"]+)".*?"list_html":\s*"(.*?)"\s*,\s*"page_link"',
    html,
    re.S,
)

if not matches:
    raise Exception("단어 데이터를 찾을 수 없습니다.")

date_label, list_html = matches[-1]

list_html = list_html.replace('\\"', '"')
list_html = list_html.replace("\\n", "")

soup = BeautifulSoup(list_html, "html.parser")

for item in soup.select("li.word_item"):
    word_el = item.select_one("a.word strong")
    mean_el = item.select_one(".mean")

    if not word_el or not mean_el:
        continue

    word = word_el.text.strip()
    meaning = mean_el.text.strip()

    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "단어": {
                "title": [
                    {
                        "text": {
                            "content": word
                        }
                    }
                ]
            },
            "뜻": {
                "rich_text": [
                    {
                        "text": {
                            "content": meaning
                        }
                    }
                ]
            },
            "날짜": {
                "date": {
                    "start": datetime.now().strftime("%Y-%m-%d")
                }
            }
        }
    )

print("업로드 완료")
