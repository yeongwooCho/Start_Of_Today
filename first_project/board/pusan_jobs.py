import requests
from bs4 import BeautifulSoup
pageChar = 100

URL = f"https://cse.pusan.ac.kr/cse/14667/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGY3NlJTJGMjYxNiUyRmFydGNsTGlzdC5kbyUzRmJic09wZW5XcmRTZXElM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZzcmNoQ29sdW1uJTNEJTI2cGFnZSUzRD{chr(pageChar)}lMjZzcmNoV3JkJTNEJTI2cmdzQmduZGVTdHIlM0QlMjZiYnNDbFNlcSUzRCUyNnJn"


def extract(html, html2):

    title = html.find("strong").string
    link = html.find("a")["href"]
    date = html2.string
    return {'num': '3', "title": title, "rate": date, "link": f"http://cse.pusan.ac.kr{link}"}


def extracts():
    emps = []
    pageChar = 65

    for page in range(2):
        pageChar += 4
        result = requests.get(
            f"https://cse.pusan.ac.kr/cse/14667/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGY3NlJTJGMjYxNiUyRmFydGNsTGlzdC5kbyUzRmJic09wZW5XcmRTZXElM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZzcmNoQ29sdW1uJTNEJTI2cGFnZSUzRD{chr(pageChar)}lMjZzcmNoV3JkJTNEJTI2cmdzQmduZGVTdHIlM0QlMjZiYnNDbFNlcSUzRCUyNnJn")

        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("td", {"class": "_artclTdTitle"})[6:]
        results2 = soup.find_all("td", {"class": "_artclTdRdate"})[6:]
        i = 0
        for result in results:
            emp = extract(result, results2[i])
            emps.append(emp)
            i += 1

    return emps


def get_emps():
    emps = extracts()
    return emps


if __name__ == '__main__':
    emp = get_emps()
    print(emp)
