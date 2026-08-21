# 정규표현식
import re  # 정규표현식 지원 모듈 로딩

ss = "1234 abc가나다abcABC_1234555실습중78입니다_6'Python is fun"
print(ss)
print(re.findall("123", ss)) # re.findall(패턴, 대상문자열) ['123', '123']
print(re.findall(r"가나", ss))
print(re.findall(r"[0-9]", ss)) # ['1', '2', '3', '4', '1', '2', '3', '4', '5', '5', '5', '7', '8', '6']
print(re.findall(r"[0-9]+", ss)) # ['1234', '1234555', '78', '6'] 한 개 이상 연속적인 숫자, 숫자만 뽑고 싶을 때
print(re.findall(r"[0-9]{2}", ss)) # ['12', '34', '12', '34', '55', '78']
print(re.findall(r"[0-9]{2,3}", ss)) # ['123', '123', '455', '78']
# \n을 찾고 싶은데, 특정 명령이 실행될 수 있으므로 상항 앞에 r 붙이기

print(re.findall(r"[a b]", ss)) # [' ', 'a', 'b', 'a', 'b', ' ', ' '] 공백까지 추출
print(re.findall(r"[a-z]", ss)) # ['a', 'b', 'c', 'a', 'b', 'c', 'y', 't', 'h', 'o', 'n', 'i', 's', 'f', 'u', 'n']
print(re.findall(r"[a-z]+", ss)) # ['abc', 'abc', 'ython', 'is', 'fun']
print(re.findall(r"[가-힣]+", ss)) # ['가나다', '실습중', '입니다']

print()
print(re.findall(r"\d", ss)) # 모든 숫자 ['1', '2', '3', '4', '1', '2', '3', '4', '5', '5', '5', '7', '8', '6']
print(re.findall(r"\d+", ss)) # ['1234', '1234555', '78', '6']
print(re.findall(r"\D+", ss)) # \d의 반대, 숫자만 미포함 [' abc가나다abcABC_', '실습중', '입니다_', "'Python is fun"]

print(re.findall(r"\s", ss)) # 공백, 탭 문자와 매핑
print(re.findall(r"\s+", ss))
print(re.findall(r"\S", ss))