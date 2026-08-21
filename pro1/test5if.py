# # 조건 판단문 if
# var = 1
# if var >= 3:
#     print("크네") #  들여쓰기 된 코드: 블럭
# print("흠 크군")

# print()
# if var >= 3:
#     print("크구나")
# else:
#     print("작구나")


# print()
# money = 700
# age = 50

# if money >= 500:
#     item = "사과"
#     if age <= 30:
#         msg = "참 참"
#     else:
#         msg = "참 거짓"

# else:
#     item = "복숭아"
#     if age >= 20:
#         msg = "거짓 참"
#     else:
#         msg = "거짓 거짓"

# print(f"중복 if 수행 후 결과 : {item}, {msg}")

# print()

# #data = input("점수 입력 : ")
# #print(data, type(data)) # 89 <class 'str'> , 숫자열을 입력해도 (숫자 모양을 한)문자열로 입력됨
# #print(int(data) + 5)

# # jumsu = int(input("점수 입력 : "))
# jumsu = 88
# print(jumsu)
# if jumsu >= 90:
#     print("우수")
# elif jumsu >= 80:
#     print("보통")
# else:
#     print('저조')


jum = 80
if 90 <= jum <=100:
    print("A")
elif 70 <= jum <90:
    print("B")
else:
    print("C")

# print("--"*10)
# names = ["홍길동", "신기해","이기자"]
# if '홍길동' in names:
#     print("친구 이름이야")
# else:
#     print("누구야")

# if (count := len(names)) >= 3:  # :=대입 표현식
#     print(f"인원수가 {count}명 이므로 단체 할인 적용")
# else:
#     print("ㅠㅠ")


# scores = [95, 88, 76, 92, 81]
# if (avg := sum(scores) / len(scores)) >= 80:
#     print(f"우수반 평균 점수 : {avg}")

# print()
# print("삼항 연산")
# a = "kbs"
# b = 9 if a == "kbs" else 11
# # if a == "kbs":
# #     b = 9
# # else:
# #     b = 11
# print("b : ", b)

# a = 11
# b = "mbc" if a == 9 else "kbs"
# print("b :", b)

# a = 3
# print(0 if a < 5 else 1 if a<10 else 2) # 조건 1이 참이면 0, 조건 1이 거짓 & 조건 2가 참이면 1, 둘다 거짓이면 2




# print("끝")