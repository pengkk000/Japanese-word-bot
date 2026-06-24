import requests
from bs4 import BeautifulSoup
from pykakasi import kakasi
from datetime import date

# -------------------------
# 일본어 → 로마자
# -------------------------

kks = kakasi()

def to_romaji(text):
    return "".join(item["hepburn"] for item in kks.convert(text))


# -------------------------
# 로마자 → 한국어식 발음
# -------------------------

def romaji_to_korean(romaji):
    r = romaji.lower()

    # 긴 음절 먼저
    replacements = [
        ("kyo", "쿄"),
        ("kyu", "큐"),
        ("kya", "캬"),

        ("sho", "쇼"),
        ("shu", "슈"),
        ("sha", "샤"),

        ("cho", "쵸"),
        ("chu", "츄"),
        ("cha", "챠"),

        ("ryo", "료"),
        ("ryu", "류"),
        ("rya", "랴"),

        ("nyo", "뇨"),
        ("nyu", "뉴"),
        ("nya", "냐"),

        ("hyo", "효"),
        ("hyu", "휴"),
        ("hya", "햐"),

        ("myo", "묘"),
        ("myu", "뮤"),
        ("mya", "먀"),

        ("gyo", "교"),
        ("gyu", "규"),
        ("gya", "갸"),

        ("byo", "뵤"),
        ("byu", "뷰"),
        ("bya", "뱌"),

        ("pyo", "표"),
        ("pyu", "퓨"),
        ("pya", "퍄"),

        ("jo", "죠"),
        ("ju", "쥬"),
        ("ja", "쟈"),
    ]

    for a, b in replacements:
        r = r.replace(a, b)

    singles = [
        ("ka", "카"), ("ki", "키"), ("ku", "쿠"), ("ke", "케"), ("ko", "코"),
        ("sa", "사"), ("shi", "시"), ("su", "스"), ("se", "세"), ("so", "소"),
        ("ta", "타"), ("chi", "치"), ("tsu", "츠"), ("te", "테"), ("to", "토"),
        ("na", "나"), ("ni", "니"), ("nu", "누"), ("ne", "네"), ("no", "노"),
        ("ha", "하"), ("hi", "히"), ("fu", "후"), ("he", "헤"), ("ho", "호"),
        ("ma", "마"), ("mi", "미"), ("mu", "무"), ("me", "메"), ("mo", "모"),
        ("ya", "야"), ("yu", "유"), ("yo", "요"),
        ("ra", "라"), ("ri", "리"), ("ru", "루"), ("re", "레"), ("ro", "로"),
        ("wa", "와"), ("wo", "오"),

        ("ga", "가"), ("gi", "기"), ("gu", "구"), ("ge", "게"), ("go", "고"),
        ("za", "자"), ("ji", "지"), ("zu", "즈"), ("ze", "제"), ("zo", "조"),
        ("da", "다"), ("de", "데"), ("do", "도"),
        ("ba", "바"), ("bi", "비"), ("bu", "부"), ("be", "베"), ("bo", "보"),
        ("pa", "파"), ("pi", "피"), ("pu", "푸"), ("pe", "페"), ("po", "포"),

        ("a", "아"),
        ("i", "이"),
        ("u", "우"),
        ("e", "에"),
        ("o", "오"),

        ("n", "ㄴ"),
    ]

    for a, b in singles:
        r = r.replace(a, b)

    return r


# -------------------------
# 크롤링
# -------------------------

url = "https://wquiz.dict.naver.com/jakodict/today/words.dict"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

soup = BeautifulSoup(html, "html.parser")

cards = soup.select(".word_list .word_card")

words = []

for card in cards:

    word = "".join(
        span.get_text(strip=True)
        for span in card.select(".word_card_title .letter")
    )

    meaning_el = card.select_one(".mean_text")
    level_el = card.select_one(".label")

    meaning = meaning_el.get_text(strip=True) if meaning_el else ""
    level = level_el.get_text(strip=True) if level_el else ""

    romaji = to_romaji(word)
    korean = romaji_to_korean(romaji)

    words.append({
        "word": word,
        "reading": f"{korean} ({romaji})",
        "meaning": meaning,
        "level": level,
        "date": str(date.today())
    })

for w in words:
    print(w)
