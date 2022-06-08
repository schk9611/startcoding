from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

# 브라우저 생성
browser = webdriver.Chrome('/Users/songyu/Documents/chromedriver')

# 웹 사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10)  # 로딩이 끝날 때까지 10초까지 기다린다

# 쇼핑 메뉴 클릭
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

# 검색창 클릭
search = browser.find_element_by_css_selector(
    'input._searchInput_search_input_QXUFf')
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 파일 생성
f = open('/Users/songyu/Documents/projects/python-projects/startcoding/data.csv',
         'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)

# 상품 정보 div
# find_element가 아닌 find_elements로 여러 값을 가져올 수 있다.(주의)
items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")


for item in items:
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text
    # 간혹 값이 없어 오류가 생길 수 있는데 이럴 경우에는 try-except 구문을 사용하자
    try:
        price = item.find_element_by_css_selector(".price_num__2WUXn").text
    except:
        price = "판매중단"
    link = item.find_element_by_css_selector(
        ".basicList_title__3P9Q7 > a").get_attribute('href')
    print(name, price, link)
    csvWriter.writerow([name, price, link])

# 파일 닫기
f.close()
