# 재귀함수 : 함수가 자기 자신을 호출 - 반복 처리 가능

def countDown(n):
    if n == 0:
        print("완료")
        return
    else:
        print(n, end = " ")
        countDown(n - 1)

countDown(5)

print('\n---1부터 n까지의 정수의 합 구하기 ---')
def totFunc(n):
    if n == 1:
            print("완료")
            return 1
    return n + totFunc(n - 1) 

result = totFunc(10)
print("result : ", result)

print('\n--- 팩토리얼 계산하기 ---')

def factFunc(a):
    if a == 1:return 1
    print(a)
    return a * factFunc(a - 1)

result2 = factFunc(5)
print("resuit2 : ", result2)