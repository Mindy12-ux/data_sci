# # 반복문 for
# # for target in object: 
# #   statement

# # for i in [1,2,3,4,5]:
# #     print(i, end=" ")

# # for i in (1,2,3,4,5):
# #     print(i, end=" ")

# # for i in {1,2,3,4,5}:
# #     print(i, end=" ")

#     # 리스트, 튜플, 셋 모두 사용 가능

# print("분산 / 표준편차")

# numbers = [1,3,5,7,9]
# # numbers = [3,4,5,6,9]
# # numbers = [-3,4,5,7,12]
# # 평균이 모두 동일

# tot = 0
# for a in numbers:
#     tot += a

# print(f"합은 {tot}, 평균은{tot/len(numbers)}")

# avg = tot/len(numbers)

# #편차제곱의 합

# hap = 0
# for i in numbers:
#     hap += (i-avg)**2

# print(f"편차제곱의 합 : {hap}")
# vari = hap / len(numbers)
# print("분산 : ", vari)
# print("표준편차 : ", vari ** 0.5)

# print()

# colors = ["빨강","초록", "파랑"]

# for v in colors:
#     print(v, end = " ")

# print()

# print("iter() : 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어 주는 함수")
# iterator = iter(colors)
# for v in iterator:
#     print(v, end = " ")

# print()
# for idx, d in enumerate(colors, start = 1):
#     print(idx, " ", d)

# # enumerate : 인덱스를 붙여서 객체를 하나씩 꺼내줌, 인덱스와 값을 반환, idx = 인덱스 번호, \
# # d = 객체 이름

# print("\n사전형 --- ")
# datas = {'python' : "만능언어", "Java":"웹용언어", "mariadb":"RDBMS"}
# print(datas.items()) 
# #[('python', '만능언어'), ('Java', '웹용언어'), ('mariadb', 'RDBMS')] / 리스트 안의 튜플로 반환
# for i in datas.items():
#     print(i[0], "~~", i[1]) 
# # python ~~ 만능언어
# # Java ~~ 웹용언어
# # mariadb ~~ RDBMS

# for k, v in datas.items():
#     print(k, "~~", v)

# for k in datas.keys():
#     print(k, end =" ")
# print()
# for v in datas.values():
#     print(v, end =" ")    

# print()

# print("\n다중 for ---------")

# for n in [2,3]:
#     print(f"{n}단 ~~~ ")
#     for su in range(1,10):
#         print(f"{n} * {su} = {n * su}")

# print()
# print("\nfor : continue, break ---------")
# nums = [1,2,3,4,5]
# for i in nums:
#     if i ==2 : continue
#     #if i ==4 : break
#     print(i, end =" ")
# else:
#     print("정상 종료")

# print("\n\n정규표현식 + for 연습")
message = """
이재명 대통령은 18일 한미 연합군사훈련인 ‘을지 자유의 방패’(UFS) 기간 국무회의에서 “전시작전권의 임기 내 환수를 당초 정부 계획에 따라 차질없이 추진해 나가야겠다”고 못 박았다.

이 대통령은 이날 오전 청와대에서 을지1 및 제36회 국무회의를 주재, 모두발언으로 “이번 을지연습 과정을 통해 우리 방위태세를 보다 면밀하게 점검, 보완하고 또 국가의 총체적 위기 대응 역량을 한층 더 강화해나가야겟다”면서도 이같이 말했다.

이 대통령은 “대한민국은 우리 국민 여러분께서 너무 잘 아시는 것처럼 세계 군사력 5위로 평가된다”며 “방산 역량이 글로벌 4강으로 평가되기도 하고, 특히 대한민국 국방비 지출 수준이 북한의 연간 총생산, 국민 총생산의 1.4배”라고 전제했다.
이재명 대통령은 18일 한미 연합군사훈련인 ‘을지 자유의 방패’(UFS) 기간 국무회의에서 이재명 대통령 apple @#$%232  2#
"""
import re
message2 = re.sub(r"[^가-힣\s]", '', message) # 패턴과 일치하는 문자열을 다른 문자열('', 없애 버리기)로 치환
print(message2, type(message2))

# message3 = message2.split(" ") # 공백을 기준으로 문자열 분리
# print(message3, len(message3))

#  for문과 dict를 활용하여 단어별 빈도수 출력
# cou = {}

# for i in message3:
#     if i in cou:
#         cou[i] += 1 #같은 단어가 있으면 누적
#     else:
#         cou[i] = 1 #최초 단어일 경우 "단어 : 1"

# print(cou)

# print("정규 표현식 좀 더 ...")
# for imsi in ["111-1234", "일이삼-일이삼사", "222-1234", "333&1234"]:
#     if re.match(r"^\d{3}-\d{4}$", imsi):
#         print(imsi, "전화번호 맞네")

#     else:
#         print(imsi, "전화번호 아니야")



# print("\ncomprehension : 반복문 + 조건문 + 값 생성을 한 줄로 표현")
# a = [1,2,3,4,5,6,7,8,9,10]
# li = []
# for i in a:
#     if i % 2 == 0:
#         li.append(i)
# print(li)

# print(list(i for i in a if i % 2 == 0)) # [2, 4, 6, 8, 10], comprehension

print()
datas = [1,2,"a",True, 3.0]
li2 = [i for i in datas if type(i) == int]
print(li2)

li2 = [i for i in datas if type(i) == int]
# print()
# id_name = {1:"tom", 2:"james"}
# name_id = {val : key for key, val in id_name.items()}
# print(name_id)



# print()
# aa = [(1,2),(3,4),(5,6)]
# for a, b in aa:
#     print(a + b)


# print(*[a + b for a, b in aa], sep ="\n")
# # 위 두개의 결과는 동일

# print("\n수열 생성 : range()")
# print(list(range(1, 6)))
# print(tuple(range(1, 6)))
# print(set(range(1, 6)))
# print(list(range(6))) # [0, 1, 2, 3, 4, 5]
# print(list(range(-10, -100, -20)))
# print()

# for i in range(6):
#     print(i, end = ", ")
# print()
# for _ in range(6):
#     print("반복", end = " ")  # 반복 반복 반복 반복 반복 반복

# print("1 ~ 10까지 정수 합")
# tot = 0
# for i in range(1, 101):
#     tot += i
# print("tot :", tot, sum(range(1, 101)))

# for i in range(1, 10):
#     print(f"2 * {i} = {2*i}")

# print("2 ~ 9 구구단 출력 (단은 행단위 출력)")
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i*j}", end =" ")
#     print()

# print()
# print("주사위를 두 번 던져 나온 숫자들의 합이 4의 배수가 되는 경우만 출력")
# for i in range(6):
#     n1 = i + 1
#     for j in range(6):
#         n2 = j + 1
#         n = n1 + n2
#         if n % 4 == 0:
#             print(n1, n2)
# print()
# for i in range(1, 7):
#     for j in range(1, 7):
#         hap = i + j
#         if hap % 4 == 0:
#             print(i, j)