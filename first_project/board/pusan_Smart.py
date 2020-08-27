from bs4 import BeautifulSoup
from selenium import webdriver


def extract_smarts():
    url = "https://e-onestop.pusan.ac.kr/menu/bbs/notice/list?menuId=20001104&rMenu=12"
    options = webdriver.ChromeOptions()
    options.headless = True

    browser = webdriver.Chrome(
        r"C:\Users\jyy02\OneDrive\Desktop\project\First_Project\first_project\chromedriver", options=options)
    browser.get(url)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    results = soup.find('table', attrs={'id': 'bbs'}).find(
        'tbody').find_all('tr')

    smarts = []
    for result in results:
        datas = result.find_all('td')

        title = datas[1].a.get_text().strip()
        rate = datas[2].get_text().strip().replace('-', '.')
        link = '#'
        smarts.append(
            {'num': '1', 'title': title, 'rate': rate, 'link': link}
        )

    browser.quit()
    return smarts


def get_smarts():
    smarts = extract_smarts()
    return smarts


if __name__ == '__main__':
    bus = get_smarts()
    print(bus)
