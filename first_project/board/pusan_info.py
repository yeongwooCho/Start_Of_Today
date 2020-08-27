import requests
from bs4 import BeautifulSoup


LIMIT = 50
URL = "http://www.busanit.or.kr/board/list.asp?bcode=notice_e&sword=&search_txt=&ipage="


def extract_busanit(html):
    title = html.find("td", {"class": "subject"}).find('a')["title"].strip()
    rate = list(html.find_all("td", recursive=False))[
        2].string.replace('-', '.')
    link = html.find("td", {"class": "subject"}).find('a')["href"]
    return {
        'num': '4',
        "title": title,
        "rate": rate,
        "link": f"http://www.busanit.or.kr/board/{link}"
    }


def extract_busanits():
    busanits = []
    for page in range(2):
        result = requests.get(f"{URL}{page + 1}")
        soup = BeautifulSoup(result.content.decode(
            'UTF-8', 'replace'), 'html.parser')
        results = soup.find("div", {"class": "content_sub"}).find(
            "table", {"class": "bbs_ltype"}).find("tbody").find_all("tr")

        for result in results:
            busanit = extract_busanit(result)
            busanits.append(busanit)
    return busanits


def get_busanits():
    busanits = extract_busanits()
    return busanits


if __name__ == '__main__':
    bus = get_busanits()
    print(bus)
