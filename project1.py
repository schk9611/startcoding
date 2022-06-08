import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# soup에 저장된 html 중 news_tit 클래스를 가진 태그를 모두 가져와 저장
links = soup.select(".news_tit")  # select 함수는 가져온 값들을 리스트로 저장한다
for link in links:
    title = link.text  # 태그 안에 텍스트 요소를 가져온다
    url = link.attrs['href']  # href의 속성값을 가져온다
    print(title, url)
