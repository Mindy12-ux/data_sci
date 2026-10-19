# BeautifulSoup 객체 메소드 이해

from bs4 import BeautifulSoup

html_page = '''
<html><body>
<h1>제목태그</h1>
<p>웹 문서 연습</p>
<p>원하는 자료 읽기</p>
</body></html>
'''
print(type(html_page))  # <class 'str'>, type이 str인 상태에서는 beautifulsoup의 메소드를 사용할 수 없음
soup = BeautifulSoup(html_page, 'html.parser')
print(type(soup))   # <class 'bs4.BeautifulSoup'>, beautifulsoup이 제공하는 메소드를 사용할 수 있음
print()
h1 = soup.html.body.h1
print('h1: ', h1.string)
p1 = soup.html.body.p  # 최초의 p
print("p1 : ", p1.string)
p2 = p1.next_sibling.next_sibling   # 두 번째 p, DOM을 이용한 접근
print('p2 : ', p2.string)

print('\n-- find() method 사용-----')
html_page2 = '''
<html><body>
<h1 id='title'>제목 태그 출력</h1> <!-- 제목 <b>태그</b> 출력 -->
<p>웹문서 연습</p>
<p id='my' class='our'>원하는 자료 확인</p>
</body></html>
'''
soup2 = BeautifulSoup(html_page2, 'html.parser')    # html_page2를 beautifulsoup 객체로 변환
# 형식 : find(tag명, attrs, recursive, string) # recursive : 자손태그
print(soup2.p, ' ', soup2.p.string)     # <p>웹문서 연습</p>   웹문서 연습
print(soup2.find('p').string)           # 웹문서 연습
print(soup2.find(['p', 'h1']).string)   # p, h1 태그 중 먼저 나오는 태그가 선택, 둘 다 나오는게 아님
print(soup2.find(['p', 'h1']).get_text())   # get_text : 하위 태그에 있는 텍스트까지 추출
print(soup2.find('p', id='my').string)  # 원하는 자료 확인
print(soup2.find(id='title').string)
print(soup2.find(class_='our').string)
print(soup2.find(attrs={'class':'our'}).string)
print(soup2.find(attrs={'id':'my'}).string)

print('\n-- find_all(), findAll() method 사용-----')
html_page3 = '''
<html><body>
<h1 id='title'>제목 태그 출력</h1>
<p>웹문서 연습</p>
<p id='my' class='our'>원하는 자료 확인</p>
<div>
    <a href='https://www.naver.com'>naver</a></br>
    <a href='https://www.daum.com'>daum</a>
</div>
</body></html>
'''
soup3 = BeautifulSoup(html_page3, 'html.parser')
print(soup3.find_all(["a"]))    # [<a href="https ... ]
print()
print(soup3.find_all(['a', 'p']))
print()
links = soup3.find_all("a")     # [<a href="https ... ]
# print(links)
for i in links:
    href = i.attrs['href']
    text = i.text   # i.string도 가능
    print(href, ' ', text)

print('\n정규 표현식 사용 --- ')
import re
links2 = soup3.find_all(href=re.compile(r'^https'))
print(links2)

for k in links2:
    print(k.attrs['href'])

print('bugs 사이트 음악 순위 읽기 -------')
import requests
url = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
# print(response.text)
bsoup = BeautifulSoup(response.text, 'html.parser')
musics = bsoup.find_all('td', class_='check')
# print(musics)
for idx, music in enumerate(musics):
    print(f'{idx + 1}위) {music.input['title']}')





