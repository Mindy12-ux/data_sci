# with 표현식 as 변수:
#       실행문
# 파일 입출력에서는 보통 이렇게 사용
# 블록 종료시 파일 자동 close됨

try:
    # 파일 저장
    with open("ftest.txt", mode="w", encoding="utf-8") as fobj1:
        fobj1.write("파이썬에서 문서 저장\n")
        fobj1.write("with 구문은\n")
        fobj1.write("파일 작업 종료 시 자동 close됨\n")

    print("저장 완료")

    # 파일 읽기
    with open("ftest.txt", mode="r", encoding="utf-8") as obj1:
        print(obj1.read())

except Exception as a:
    print("에러는 : ", a)

print("\n\n피클링(Pickling) : 일반 객체 및 복합 개체 파일 입출력")
import pickle

try:
    dicdata = {"tom": 111-1111, "길동":222-2222}
    lidata = ["마우스", "모니터"]
    tupdata = (dicdata, lidata)

    with open("hello.dat", mode="wb") as obj3:
        pickle.dump(tupdata, obj3)  # 저장 - pickle.dump(대상, 파일객체)
        pickle.dump(lidata, obj3)
        print("특정 객체를 파일로 저장")

    print("\n피클 객체 읽기")
    with open("hello.dat", mode="rb") as obj4:
        a, b= pickle.load(obj4)
        print("a : ",a)  # a :  {'tom': -1000, '길동': -2000}
        print("b : ",b)  # b :  ['마우스', '모니터']

        c, d= pickle.load(obj4)
        print("c : ",c)  # c :  ['마우스', '모니터']
        print("d : ",d)



except Exception as a1:
    print("피클링 연습 중 오류, 그  이유 : ", a1)