import requests
from bs4 import BeautifulSoup
# pyautogui 불러오기
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요.")

# 마지막 페이지 번호를 사용자가 지정할 수 있도록 입력값을 담을 변수 생성
lastpage = pyautogui.prompt("마지막 페이지 번호를 입력해 주세요.")

# 페이지를 구분하기 위한 수
pageNum = 1

# 한 페이지에서 작동하던 코드를 각 페이지마다 작동하도록 반복문 작성
# range에서 lastpage 변수를 사용하는데 위에서 입력받은 형태는 string 타입이기 때문에 int로 형변환 시켜준다
for i in range(1, int(lastpage) * 10, 10):

    # page를 구분하기 위해 반복 제일 위에 표시
    print(f"{pageNum} 페이지 입니다.=============================")

    # url의 parameter 중 페이지와 관련된 "start=숫자"에서 숫자 부분은 변수로 만들어 페이지로 이동하도록 만든다
    response = requests.get(
        f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit")
    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title, url)

    # 반복이 끝나기 전 pageNum에 숫자 1을 더해 다음 페이지 시작할 때 기존 페이지 보다 1 증가한 수를 표현하도록 한다
    pageNum = pageNum + 1

    # 페이지 구분을 위한
    print("")
