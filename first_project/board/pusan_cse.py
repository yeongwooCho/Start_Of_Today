import requests
from bs4 import BeautifulSoup
import csv

LIMIT = 50
URL1 = f"https://cse.pusan.ac.kr/cse/14651/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGY3NlJTJGMjYwNSUyRmFydGNsTGlzdC5kbyUzRmJic09wZW5XcmRTZXElM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZzcmNoQ29sdW1uJTNEJTI2cGFnZSUzRD"
URL2 = f"lMjZzcmNoV3JkJTNEJTI2cmdzQmduZGVTdHIlM0QlMjZiYnNDbFNlcSUzRCUyNnJnc0VuZGRlU3RyJTNEJTI2"


def extract_notice(html):
    title = html.find("td", {"class": "_artclTdTitle"}
                      ).find('a').find("strong").string
    rate = html.find("td", {"class": "_artclTdRdate"}).string.strip()
    link = html.find("td", {"class": "_artclTdTitle"}).find('a')["href"]
    return {
        'num': '2',
        "title": title,
        "rate": rate,
        "link": f"https://cse.pusan.ac.kr{link}"
    }


def extract_notices():
    notices = []
    for page in range(2):
        page_alphabet = chr(69 + page*4)
        result = requests.get(f"{URL1}{page_alphabet}{URL2}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find("table", {"class": "artclTable artclHorNum1"}).find(
            "tbody").find_all("tr")

        for result in results[5:]:
            notice = extract_notice(result)
            notices.append(notice)

    return notices


def get_notices():
    notices = extract_notices()
    return notices


if __name__ == '__main__':
    no = get_notices()
    print(no)
