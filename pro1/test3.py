# 기본 자료형 : int. float, bool. complex
# 묶음 자료형 : str, list, tuple, set, dict

# str : 문자열 저장 단위, 순서가 존재함(순형), 수정이 불가함
s = "sequence"
print("길이(크기):", len(s)) # 길이(크기): 8, 8개의 바이트를 사용하고 있다는 의미임
print("포함 횟수:", s.count("e"))
print("검색 위치:", s.find("e"), s.find("e",3), s.rfind("e"))
print("첫 글자 유뮤: ", s.startswith("s"), s.startswith("a"))  

print()
ss = "mbc"
print(ss, id(ss))
ss = "abc"
print(ss, id(ss)) # mbc의 m을 a로 수정한 것이 아니라, mbc 전체가 abc로 완전히 대체된 것  

print("인덱싱과 슬라이싱")
print(s[0], s[5], s[-1])
print(s[0:4], s[:4], s[-4:-1]) # 슬라이싱, sequ sequ(0번째부터 5번째 "전"까지) enc(-4번째부터 -1번재 "전"까지)
print(s[::]) # 모두 출력
print(s[::2]) # 증가치 2
print(s[0:8:3], s[0:len(s)]) # 0번째부터 8번째 전까지 3씩 증가시켜서 출력

print("*" * 10)
# 리스트 : 다양한 종류의 자료 묶음형. 순서 존재, 수정 가능, 중복 허용
a = [1,2,3] # 다양한 종류의 데이터형이 들어올 수 있다
print(type(a))
print(a, a[0], a[0:2])
b = [10, a, 10, 20.5, True, "문자열"]
print(b, b[0], b[1], b[1][1])
print()
family = ["엄마", "아빠", "나", "여동생"]
print(family, id(family)) # ['엄마', '아빠', '나', '여동생'] 2866086705216
family.append("남동생") # 추가
print(family, id(family)) # ['엄마', '아빠', '나', '여동생', '남동생'] \2866086705216 
# 주소가 동일함, 수정이 허용됨
family.remove("나") # 삭제
print(family) # '엄마', '아빠', '여동생', '남동생']
family.insert(0, "할머니") # 삽입
print(family)
family.extend(["삼촌",'고모','조카']) # 추가
print(family)
family += ["이모"] # 추가(누적을 이용한 추가)
print(family)

family.remove("아빠") # 삭제
del family[2]
print(family)

print()
kbs = ["123",'34', '234']
kbs.sort()  # 문자열 정렬
print(kbs) # ['123', '234', '34'], 사전형으로 정렬
mbc = [123,34, 234]
mbc.sort()
print(mbc) # [34, 123, 234],  오름차순으로 정렬(ascending),  리스트 값 순서가 바뀜
mbc.sort(reverse = True)
print(mbc) # [234, 123, 34],  내림차순으로 정렬(decending)
print()
sbs = [123, 34, 234]
ytn = sorted(sbs) # 원본의 변화 없이 정렬된 값을 새로운 변수에 치환
print(ytn)
print(sbs)

print("*" * 10)
# tuple : 리스트와 유사, 읽기 전용, 수정이 불가능함
t = (1,2,3,4)
t = 1,2,3,4 # 소괄호 생략 가능, 원소가 복수일때만 가능
print(t, type(t))

k = (1)
print(k, type(k)) # 1 <class 'int'>, 데이터 값이 하나일때, 튜플을 만들고 싶으면 ,를 찍어줘야 됨
k = (1,)
print(k, type(k)) # (1,) <class 'tuple'>

print(t, t[0], t[1:3])
# t[0] = 9 , 에러, 튜플은 수정이 불가능함.

# 튜블 값 수정시 리스트로 형변환 사용

imsi = list(t) # type 변환
print(type(imsi)) # <class 'list'>
imsi[0] = 9
t = tuple(imsi)
print(t, type(t)) # (9, 2, 3, 4) <class 'tuple'>

print("--"*10)

# set : 순서 없음, 중복 불가, 수정 가능
ss = {1,2,3, 2}
print(ss, type(ss)) # {1, 2, 3} <class 'set'>, 중복 데이터가 모두 사라짐, 중복 데이터를 처리할 때 유용

ss2 = {3,4}
print(ss.union(ss2)) # 합집합 , {1, 2, 3, 4}
print(ss.intersection(ss2)) # 교집합 , {3}
print(ss - ss2, ss | ss2, ss & ss2) # 차집합, 합집합, 교집합 , {1, 2} {1, 2, 3, 4} {3}
print()
ss.update({6,7})
print(ss)
ss.discard(7) # 해당 값 없으면 통과
ss.remove(6) # 해당 값 없으면 에러
print(ss)

li = ["aa", 'aa','bb',"cc", "aa"] # set의 활용, 중복된 데이터 제거
print(li)
imsi = set(li)
li = list(imsi)
print(li)

print("--"*10)
# dict : 사전 자료형 {"키":값} 형태
# 방법 1, dict 함수 사용
mydic = dict(k1 = 1, k2 = "ok", k3 = 1234)
print(mydic, type(mydic)) # {'k1': 1, 'k2': 'ok', 'k3': 1234} <class 'dict'>
# json 이 키-값 쌍으로 이루어진 데이터임, 파이썬과  json 간 자료를 주고 받을 때 dict사용

# 방법 2, {} 사용
dic = {"파이썬": "뱀", "자바":"커피", "번호":123}
print(dic, type(dic))
print(len(dic))
print(dic["자바"]) # 커피
print(dic.get('자바')) # 위와 동일, key로 값을 검색
# print(dic[0]) # 에러, 딕셔너리는 인덱싱이 불가능, 순서가 없기 때문
dic["금요일"] = "wow" #  추가
print(dic)

del dic["번호"] # 삭제
print(dic)
print(dic.keys()) # dict_keys(['파이썬', '자바', '금요일'])
print(dic.values()) # dict_values(['뱀', '커피', 'wow']) 결과값을 리스트로 반환
