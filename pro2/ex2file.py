print("파일 처리 : 입출력")
import os       # 운영체제와 관련된 기능을 제공\

try:
    print("--------파일 읽기-------")
    print(os.getcwd())  # C:\works\projects\pro2

# 읽을 파일 - C:\works\projects\pro2\ftest.txt

    #f1 = open(os.getcwd() + "\\ftest.txt", mode ="r", encoding="utf-8")
    # 만약 파일명이 ntest 여서 \ntest.txt가 되는 경우, r"\ntest.txt"로 쓸 것
    # 이때의 r은 raq string이라고 지칭함.
    f1 = open(r"ftest.txt", mode= "r", encoding="utf-8")
    # 파이썬은 구체적인 경로명을 작성하지 않아도 인식함

    print(f1)
    print(f1.read())
    f1.close()  # 작업이 끝나면 닫기 권장

    print("--------- 파일 저장 ---------")
    f2 = open(r"ftest.txt", mode="w", encoding="utf-8")
    f2.write("내 친구들\n")
    f2.write("신기해, 이기자\n")
    f2.close()
    print("파일 저장 성공")

    print("----------- 파일 내용 추가 -----------")
    f2 = open(r"ftest.txt", mode="a", encoding="utf-8")
    f2.write("\n사오정\n")
    f2.write("손오공과 저팔계\n")
    f2.close()
    print("파일 저장 성공")

    # ftest 읽기
    print("-------------")
    f4 = open("ftest.txt", mode="r", encoding="utf-8")
    print(f4.read())
    f4.close()

except Exception as e:
    print("처리 오류 : ", e)


