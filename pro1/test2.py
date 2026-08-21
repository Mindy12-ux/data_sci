# 연산자
# 치환 연산자
v1 = 3
v1 = v2 = v3 = 5
print(v1, v2, v3)

v1 = 10, 20 , 30
print("v1 : ", v1)  #v1 :  (10, 20, 30)

v1, v2 = 10, 20
print(v1, v2)   #10 20
v2, v1 = v1, v2
print(v1, v2)   #20 10, 기억장소의 값 맞교환

print("값 할당 packing")
v1, *v2 = 1,2,3,4,5
print(v1, v2)   #1 [2, 3, 4, 5], 각 변수에 하나의 값을 할당하고, *을 달고 있는 변수에 남은 것을 할당
*v1, v2 = 1,2,3,4,5
print(v1, v2)
*v1, v2, v3 = 1,2,3,4,5
print(v1, v2, v3)   #[1, 2, 3] 4 5

print('print 함수 알아보기')
print(format(123.45678, '10.3f'))
print(format(123.45678, '10.3'))
print ('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
name = "마우스"; price \
    = 5000;  #;을 붙이면 여러 개의 명령문을 한 줄에 쓸 수 있음, \를 주면 명령문을 다음줄에 이어서 쓸 수 있음
print(f"이름:{name}, 가격:{price}")  # 이름:마우스, 가격:5000, 이 방법은 많이 쓰게 될 것임
print("abc")
print("def")
print("abc", end=" ")   #abc def: " "사이에 있는 것을 출력하고 이어서 출력
print("def")

print('\n연산자 연습 계속')
print(5 + 3, 5 - 3, 5 * 3, 5 / 3, 5 // 3, 5 % 3, 5 ** 3)
print(123456789**123)
print(divmod(5,3))  #(1, 2), 몫과 나머지
print(3 + 4 * 5, (3 + 4) * 5)
# 연산자 우선순위(먼저 계산): () -> ** -> 단항 연산 -> *, /(곱하기 나누기는 우선순위가 없음, \
# 왼쪽 먼저 계산) -> +, - -> 비교연산자 -> not -> and -> or -> =

print('관계(비교) 연산자')
print( 5 > 3 , 5 == 3, 5 != 3)  # True False True

print('논리 연산자')
print( 5 > 4 and 4 < 3, 5 > 4 or 4 < 3, not(5 >= 4))    #False True False

print('문자열 더하기')
print('한' + "국" + " 만세")
print("한국" * 20)

print("누적")
a = 10
a = a + 1   #증감 연산자
a += 1
print('a는 ', a)
print(f"a는 {a}")

print('부호 변경 : ', a, a* -1, -a, --a, ---a)  # 12 -12 -12 12 -12

print('boolean 처리 : ', bool(123), bool(1), bool(-3.5), bool(False)) #True True True False
print('boolean 처리 : ', bool(0), bool(0.0), bool(False), bool(None)) # False False False False
print('boolean 처리 : ', bool([]), bool({}), bool(set())) # False False False, 유의미한 데이터가 있는 경우만 True

print('이스케이프 문자') # escape character (\) - 특별한 의미를 표현하기 위한 문자 조합
print('aa\tbb') # \의 특수성을 없애고 싶으면 구문 앞에 r을 선행해야 됨
print(r'aa\tbb')
print('aa\bbb') 
print(r'aa\bbb')
print('aa\nbb')
print(r'aa\nbb')
print('c:\a\abc.txt')
print('c:\n\abc.txt')