# 웹(donga.com)에서 특정 단어 관련 문서를 검색한 후 명사만 추출하기
# 워드클라우드 그리기
# pip install simplejson pytagcloud
# python -m pip install --upgrade pygame-ce

from bs4 import BeautifulSoup
from urllib.parse import quote
import urllib.request
from konlpy.tag import Okt
from collections import Counter     # 단어 수를 세는 라이브러리
import pytagcloud
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import koreanize_matplotlib
import webbrowser
import pandas as pd
import numpy as np
import pygame

# searchWord = input('검색어 : ')
# print(quote(searchWord))

searchWord = '가을'
target_url = 'https://www.donga.com/news/search?query=' + quote(searchWord)
source_code = urllib.request.urlopen(target_url)    # '가을'을 검색했을 때 나오는 기사 목록 페이지
# print(source_code)

soup = BeautifulSoup(source_code, 'lxml', from_encoding='utf-8')
# print(soup)

msg =''
# result = [] result가 여기서 선언되면 for문을 돌면서 값들이 중복되어 저장됨. 선언을 for문 안에서 했기 때문에 result가 계속 초기화되어 값이 중복저장되지 않는 것.

for title in soup.find_all('h4', class_='tit'):
    title_link = title.find('a')
    # print(title_link)
    article_url = title_link['href']
    # print(article_url)  # https://sports.donga.com/news/article/all/20261022/134888881/1 ... 처럼 뉴스기사 링크를 가져옴

    try:
        source_article = urllib.request.urlopen(article_url)    # 기사 목록에 있는 각각의 기사 주소
        soup2 = BeautifulSoup(source_article, 'lxml', from_encoding='utf-8')
        # print(soup2)
        contents = soup2.select('div.article_txt')
        # print(contents) # 크롤링 : 여러 페이지를 돌아다니면서 데이터를 가져오는 것, 스크래핑 : 하나의 페이지에서만 데이터를 가져오는 것
        for imsi in contents:
            item = str(imsi.find_all(string=True))  # 텍스트만 가져오기 
            msg += item

    except Exception as e:
        print('처리 오류 : ', e)

    # print(msg)
    # 형태소 분석 후 명사만 추출
okt = Okt()
nouns = okt.nouns(msg)

result = []

for n in nouns:
    if len(n) > 1:
        result.append(n)    # 두 글자 이상의 단어만 저장

# print(result)

count = Counter(result)
# print(count)
tag = count.most_common(50)
print(tag)

# 워드 클라우드 작성
# taglist = pytagcloud.make_tags(tag, maxsize=100)
# # print(taglist)  # [{'color': (188, 150, 152), 'size': 129, 'tag': '가을'},

# pytagcloud.create_tag_image(taglist, 'nlp_word.png', size=(1000, 600), 
#                             background=(0,0,0), fontname='korean', 
#                             rectangular=False)

# img = mpimg.imread('nlp_word.png')
# plt.imshow(img)
# plt.show()

# webbrowser.open('nlp_word.png')

print('--------------')
df = pd.DataFrame(count.items(), columns=['단어', '빈도수'])
print(df.head(5))

if not df.empty:
    print('\n빈도수 기준 내림차순 정렬 ---- ')
    df = df.sort_values(by='빈도수', ascending=False)
    df =df.reset_index(drop=True)
    print(df.head(5))

    print('\nPandas 기초 통계 : \n', df['빈도수'].describe())

    print('\nNumpy 기초 통계 : ')
    freq = df['빈도수'].to_numpy()
    print('전체 단어 출현 횟수 : ', np.sum(freq))
    print('평균 빈도수 : ', np.mean(freq))
    print('표준편차 : ', np.std(freq))

    print('\n상위 단어 10개로 막대 그래프')
    top10 = df.head(10).sort_values(by='빈도수')
    plt.figure(figsize=(10,6))
    plt.barh(top10['단어'], top10['빈도수'])
    plt.xlabel('단어')
    plt.ylabel('빈도수')
    plt.show()

    df.to_csv('nlp_freq.csv', index=False, encoding='utf-8')

else:
    print('분석할 단어가 없어요')
