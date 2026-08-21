# # 반복문 while 조건 : 조건이 참인 동안 블럭 수행
# a = 1
# while a <= 5:
#     print(a, end = "/")
#     a += 1
# # else: # while 은 else를 꼭 써줘야 하는건 아님, 조건에 따른 종료 시 수행
# #     print("수행 성공")

# print()
# i = 1
# while i <= 3:
#     j = 1
#     while j <= 4:
#         #print("i = " + str(i) , "j = " + str(j))
#         print(f"i = {i} j = {j}")
#         j += 1
#     i += 1


print()
print("1~100 사이의 정수 중 3의 배수의 합은?")

su = 1
hap = 0
while su <= 100:
    #print(su, end =" ") while문을 이용해 0~100 사이의 값 생성
    if su % 3 ==0:
        #print(su, end =" ") if 문을 이용해 3의 배수만 선별  
        hap += su
    su += 1
print("합은 : ", hap)

# print()
# colors = ["r","g", 'b']
# num = 0
# while num < len(colors):
#     print(colors[num])
#     num += 1


# print("if 블럭 내에 while 블럭 사용")
# import time
# print("a")
# time.sleep(2)
# print("b") # a출력 후 2초 뒤에 b 출력 


# sw = input("폭탄 스위치를 누를까요? [y/n]")
# if sw == "y" or sw == "Y":
#     count = 5
#     while 1 <= count:
#       print("%d초 남았어요"%count)
#       time.sleep(1)
#       count -= 1
# print("폭발")

# elif sw == "N" or sw == "n":
#     print("작업취소")

# else:
#     print("y 또는 n을 누르시오")


# print("\ncontinue / break")
# a = 0
# while a< 10:
#     a += 1
#     if a == 7 :break # 반복문 무조건 탈출, 이 경우 비정상 종료이기때문에, else가 찍히지 않음
#     if a == 5:continue # 아래 문을 무시하고 while로 이동, print(a)를 수행하지 않음, 따라서 5가 찍히지 않음
#     print(a)


# print("\n키보드로 정수를 입력받아 홀수, 짝수 출력(무한 반복)")
# while True:
#     mysu = int(input("확인할 정수 입력 : "))

#     if mysu == 0:
#         print("프로그램 종료")
#         break
#     elif mysu % 2 == 0:
#         print(f"{mysu}는 짝수입니다.")
#         #continue 있어도 되고 없어도 됨
#     elif mysu % 2 == 1:
#         print(f"{mysu}는 홀수입니다.")
# print("\n끝")