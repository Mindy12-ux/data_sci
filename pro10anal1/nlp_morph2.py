# 웹 문서를 읽어 형태소 분석 : 위키백과에서 단어를 검색한 결과 불러오기
# 단어 출현 횟수를 DataFrame에 저장
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib import parse    # 한글 인코딩
from konlpy.tag import Okt

okt = Okt()

# url = 'https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0'
para = parse.quote('이순신')
url = 'https://ko.wikipedia.org/wiki/' + para
print(url)

headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url=url, headers=headers)

if response.status_code == 200:
    page = response.text
    # print(page, type(page))
    soup = BeautifulSoup(page, 'html.parser')

    wordlist = []   # 형태소 분석을 통해 명사만 기억

    for item in soup.select('#mw-content-text p'):
        # print(item.string)
        if item.string != None:
            wordlist += okt.nouns(item.string)

    print('wordlist : ', wordlist)
    print('단어 수 : ', len(wordlist))
    print('중복 제거 후 단어 수 : ', len(set(wordlist)))
    print()
    word_dict = {}  # 단어의 사용 회수를 dict로 저장
    for i in wordlist:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1

    print(word_dict)

    print('Series로 출력 --- ')
    seri_list = pd.Series(wordlist)
    print(seri_list[:3])
    print(seri_list.value_counts()[:5])
    print()
    seri_dict = pd.Series(word_dict)
    print(seri_dict[:3])
    print(seri_dict.value_counts()[:5])

    print('\nDataframe으로 출력')
    df1 = pd.DataFrame(wordlist, columns=['단어'])
    print(df1.head(5))
    df2 = pd.DataFrame([word_dict.keys(), word_dict.values()])
    df2 = df2.transpose()
    df2.columns = ['단어', '빈도수']
    print(df2)

    result = df2[df2['빈도수'] >= 5]    # 빈도수가 5회 이상인 단어
    print('5회 이상 등장한 단어 : \n', result)
    print('\n전체 단어 빈도수  : \n', df2['빈도수'].sum())
    print('\n평균 출현 빈도수  : \n', df2['빈도수'].mean())



