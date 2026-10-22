# 형태소 분석
# 코퍼스(Corpus, 말뭉치) : 언어 연구, 사전 편찬, 인공지능 자연어 처리를 위해 국립국어원 같은 기관이나 연구자가 
# 실제 쓰인 언어 자료를 컴퓨터가 읽을 수 있도록 대규모로 모아 놓은 말뭉치. 
# 정의 : 사람이 실제로 쓰고 말한 언어 자료를 수집, 정제한 데이터.
# 자연어 처리(NLP)에서 토큰(Token)이란 컴퓨터가 텍스트를 이해하고 연산할 수 있도록 나누는 의미 있는 최소 단위를 뜻하며, 
# 이 단위를 나누는 과정을 토큰화(Tokenization)라고 합니다. 글자, 단어, 형태소, 또는 단어의 조각(Subword) 등이 토큰이 될 수 있습니다
# 토큰의 주요 유형 : 단어 토큰(word token), 형태소 토큰(morpheme token), 문자 토큰(character token)

# 영어 토큰(Token)화
import nltk
from nltk.tokenize import word_tokenize

# 최초 실행 시 필요한 데이터 다운로드
# nltk.download('punkt')
# nltk.download('punkt_tab')

text = "I am studying Python with my friends at my room."

# 1. 토큰화
tokens = word_tokenize(text)
print(tokens) # ['I', 'am', 'studying', ...]
print()
# 품사 태깅
pos_tags = nltk.pos_tag(tokens)
print(pos_tags) # [('I', 'PRP'), ('am', 'VBP'), ...]


# 2. 한국어 토큰화
from konlpy.tag import Okt, Kkma, Komoran

text ='나는 오늘 아침에 학교에 갔다. 가는 길에 피어있던 국화가 너무 예뻤다.'

print('\n\nOkt--------------')
okt = Okt()
print('형태소 : ', okt.morphs(text))    # 형태소 :  ['나', '는', '오늘',
print('품사 태깅 : ', okt.pos(text))    # 품사 태깅 :  [('나', 'Noun'), ('는', 'Josa'),
print('형태소 (어간 포함) : ', okt.morphs(text, stem=True)) # 원형 출력 # 형태소 (어간 포함) :  ['나', '는', ... '가다', '.', '가다', '길', '에', '피다'
print('명사 추출 : ', okt.nouns(text))  # 명사 추출 :  ['나', '오늘', '아침', '학교', '길', '국화']

print('\n\nkkma--------------')
kkma = Kkma()
print('형태소 : ', kkma.morphs(text))   
print('품사 태깅 : ', kkma.pos(text))   
print('명사 추출 : ', kkma.nouns(text))

print('\n\nKomoran--------------')
komoran = Komoran()
print('형태소 : ', komoran.morphs(text))   
print('품사 태깅 : ', komoran.pos(text))   
print('명사 추출 : ', komoran.nouns(text))


