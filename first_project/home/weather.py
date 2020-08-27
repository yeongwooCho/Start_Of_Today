# Project : 웹 스크래핑을 이용하여 나만의 비서를 만든다
# 1. 네이버에서 오늘 서울의 날씨 정보를 가져온다
# 2. 헤드라인 뉴스 3건을 가져온다

import requests
from bs4 import BeautifulSoup


# [네이버 오늘의 날씨]
def today():
    url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%B6%80%EC%82%B0%EB%82%A0%EC%94%A8'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    table = soup.find('div', attrs={'class': 'info_data'})

    state = table.find('li').get_text().strip()
    cur = table.p.span.get_text().strip()
    max_min = soup.find('li', attrs={'class', "date_info today"}).find(
        'dd').find_all('span')
    rains = soup.find('li', attrs={'class', "date_info today"}).find_all(
        'span', attrs={'class': 'num'})

    dic = {'state': state, 'cur': cur, 'min': max_min[0].get_text(
    )+'℃', 'max': max_min[2].get_text()+'℃', 'rain_mo': rains[0].get_text()+'%', 'rain_ni': rains[1].get_text()+'%'}
    return dic
    # print(state)
    # print(f"{cur}℃\t( 최저 {max_min[0].get_text()}℃ / 최고 {max_min[2].get_text()}℃ )")
    # print(f'오전 강수확률 {rains[0].get_text()}% / 오후 강수확률 {rains[1].get_text()}%')

    # 구름많음, 어제보다 0˚ 높아요
    # 28℃     ( 최저 26℃ / 최고 30℃ )
    # 오전 강수확률 80% / 오후 강수확률 70%

# =================================================================================================================
# =================================================================================================================


# [헤드라인 뉴스]
def news():
    url = 'https://news.naver.com/'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    artis = soup.find_all('div', attrs={'class': 'hdline_article_tit'})
    datas = []
    for ind, arti in enumerate(artis):
        # print(f"{ind}. {arti.get_text().strip()}")
        # print(f"(링크 : {arti.a['href']})")
        datas.append({'ind': ind, 'title': arti.get_text().strip(),
                      'link': arti.a['href']})

    return datas
    # 0. 정부·의협 강대강 충돌…출구 없는 의사 총파업
    # (링크 : /main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=025&aid=0003029657)
    # 1. “이방카는 뱀이에요”…트럼프 모녀 ‘끝장’ 궁중암투
    # (링크 : /main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=005&aid=0001355945)
    # 2. 미 ‘흑인 피격’ 항의시위 사흘째, 주민끼리 총격 2명 사망
    # (링크 : /main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=025&aid=0003029590)
    # 3. 태풍 ‘바비’ 북상 서울 전역 태풍주의보…중대본 비상 3단계 격상(종합)
    # (링크 : /main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=081&aid=0003118866)
    # 4. 출입기자 확진에 국회의사당 27일 폐쇄…이해찬·김태년 자가격리
    # (링크 : /main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=030&aid=0002899831)
