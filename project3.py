from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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
