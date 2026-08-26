# 예외처리 : 파일, 네트워크, 데이터베이스 작업, 실행오류 등의 에러에 대해
# try~ except 구문을 실행하여 프로그램이 종료되지 않도록 하는 문법

# try에는 오류가 발생할 가능성이 있는 코드를 작성하고,
# except에는 해당 오류가 발생했을 때 어떻게 처리할지를 작성한다.

# try:
#   실행할 코드
# ...
# except 예외종류:
#   오류 처리 코드
# finally:
#   오류 유무와 상관없이 처리할 구문 (반드시 시행할 코드)

def divideFunc(a, b):
    return a / b

print("이런 저런 작업을 하다가 ...")

try:
    c = divideFunc(5,1)
    print(c)
    aa = [1,2]
    print(aa[3])
    # 파일 읽기
    open("c:/work/abc.txt")

# 여러 예외를 포괄적으로 처리

except Exception:
    print("에러가 발생했습니다. 다시 한 번 확인해주세요")

finally:
    print("에러 유무에 상관없이 반드시 수행됨")

print("프로그램 종료")