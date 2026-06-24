import requests
from bs4 import BeautifulSoup

url = "https://wquiz.dict.naver.com/jakodict/today/words.dict"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

soup = BeautifulSoup(html, "html.parser")

cards = soup.select(".word_list .word_card")

for idx, card in enumerate(cards, 1):

    word = "".join(
        span.get_text(strip=True)
        for span in card.select(".word_card_title .letter")
    )

    meaning_el = card.select_one(".mean_text")
    level_el = card.select_one(".label")

    meaning = meaning_el.get_text(strip=True) if meaning_el else ""
    level = level_el.get_text(strip=True) if level_el else ""

    print(f"[{idx}]")
    print("단어 :", word)
    print("뜻   :", meaning)
    print("레벨 :", level)
    print()
