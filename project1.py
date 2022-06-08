import requests
from bs4 import BeautifulSoup
# pyautogui 불러오기
import pyautogui

# pyautogui의 prompt 함수를 통해 입력창 띄워 입력 받기
keyword = pyautogui.prompt("검색어를 입력하세요.")

# f string을 사용해 문자열 안 변수 사용하기
response = requests.get(
    f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")
for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url)
