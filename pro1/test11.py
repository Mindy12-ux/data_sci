# 매개변수 유형
# 위치 매개변수 : 인수와 순서대로 대응
# 기본값 매개변수 : 매개변수에 입력값이 없으면 기본값
# 키워드 매개변수 : 실인수와 가인수 간 동일 이름으로 대응
# 가변 매개변수 : 인수의 갯수가 동적인 경우

def showGugu(start, end=5):
    for dan in range(start, end + 1, 1):
        print(str(dan) + '단 출력')
        for i in range(1, 10):
            print(f"{dan} * {i} = {dan*i}", end = " ")

        print()



showGugu(2,3) #위치 매개변수
print()
showGugu(2) # 기본값 매개변수, 기본값 5를 사용
print()
showGugu(start = 7, end= 9) # 키워드 매개변수
print()
showGugu(end = 9, start= 7) # 키워드 매개변수
print()
showGugu(7, end= 9) # 키워드 매개변수, 에러없이 실행됨
# showGugu(start = 7, 9)  에러, 위치변수는 키워드 인수 뒤에 나타날 수 없음

print("가변 매개변수 ~~~~~")
def func1(*ar): # * : 여러 개의 인자를 tuple로 묶어서 받겠다는 의미
    print(ar)
    for i in ar:
        print("밥 : " +i)

func1("김밥")  # ('김밥',) 튜플로 반환되는 것을 볼 수 있음
func1("김밥", "비빔밥") # ('김밥', '비빔밥')

print()
def func2(a, *ar):
#def func2(*a, ar):   # 이건 에러남
    print(a)
    print(ar)

func2("김밥","비빔밥", "주먹밥")  # 김밥, ('비빔밥', '주먹밥')

print()
def func3(w, h, **other):  # **은 딕셔너리로 반환됨 
    print(f"몸무게 : {w}, 신장 : {h}")
    print(f"기타 : {other}")

func3(80, 180, irum="신기해", nai=33)  # 무게 : 80, 신장 : 180, 기타 : {'irum': '신기해', 'nai': 33} 
# 변수를 넣을 때는 딕셔너리 타입으로 넣으면 안 됨

print()
def func4(a,b,*c,**d):
    print(a,b)
    print(c)
    print(d)

func4(1,2)
func4(1,2,3,4,5, kbs =9 , mbc = 10)

print()

# type hint : 함수의 인자와 반환 값에 대한 type을 적어 가독성을 향상해줌
# num:int , -> dict[str, int] 강제성은 없음, num은 숫자로 넣으라고 다른 사람에게 힌트를 주는 것 뿐.
# type에 대한 강제성은 없다.

def typeFunc(num:int, data:list[str]) -> dict[str, int]:
    print(num, data)
    result = {}
    for idx, item in enumerate(data, start = 1):
        print(f"idx:{idx}, item:{item}")
        result[item] = idx

    return result

rdata = typeFunc("1", ["일", "이","삼"])
print(rdata)




