# # 1번 문제(완)
# a = 1
# sum = 0
# li = []
# while a <= 100:
#     if a % 2 !=0 and a % 3 == 0:
#         sum += a
#         li.append(a)
#     a += 1
# print(li)
# print("합계 : ",sum)


# 2번 문제(완)

i = 2

# while i <=5:
#     j = 1
#     while j <= 9:
#         print(f"{i} x {j} = ", i*j)
#         j += 1
#     i += 1
#     print("--"*8)

# 3번 문제(완)

# i = 1
# sum = 0
# while i <= 100:
#     #print(i)
#     if i % 2 == 0:
#         sum += i
#     else:
#         sum -= i

#     i += 1
# print(sum)

# 4번 문제(완)
# a = 1
# sum = 0

# while a <= 99:
#     if a % 2 ==1 and (a //2) % 2 == 0:
#         #print(a)
#         sum -= a
#     elif  a % 2 ==1 and (a //2) % 2 == 1:
#         #print(a)
#         sum += a
#     a += 1
# print(sum)

# #4번 다른 풀이
# n = 1
# sign = -1
# total = 0

# while n <= 100:
#     value = n * sign
#     total += value

#     sign *= -1
#     n += 2
# print(total)

# 5번 문제(완)

# li = []
# a = 1

# while a <= 100:
#     b = str(a)
#     #print(len(b))
    
    
#     if len(b) ==2:
#         i = int(b[0])
#         j = int(b[1])  
#         if (i+j) >= 10:
#             print(f"{i} + {j} =", i+j)
#             li.append(b)
#     a += 1
        
# print(li)
    
# a = 100
# b = str(a)
# print(b[1])

# 6번 문제(완)

# a = 1
# sum = 0

# while True:
#     sum += a
#     print(sum)
#     a += 1
#     if sum >= 1000:
#         print(f"a : {a} 누적합 : {sum}")
#         break

# 7번 문제(완)

# i = 2

# while i <= 9:
#     j =1
#     while j <= 9:
#         if i*j < 30:
#             print(f"{i} x {j} = ",i*j)
#         j += 1
#     i += 1

# 8번 문제 (완)

# a = 2
# li = []
# while a <= 1000:
#     b = 2
#     while b <= a:
#         if a % b == 0 and a != b:
#             b += (a-b) +1
#             continue

#         elif a % b != 0:
#             b += 1
#             continue

#         elif a % b == 0 and a == b:
#             li.append(a)
#             b += 1

#     a += 1
        
# print(li)


# 9번 문제(완)

# a = 1
# while a<= 50:
#     if a % 3 == 0:
#         a += 1
#         continue
#     print(a)
#     a += 1

# 10번 문제(완)

# a = 1
# sum = 0
# li = []
# while a <= 100:
#     if a % 4 == 0 or a % 6 ==0:
#         a += 1
#         continue
#     elif a % 5 ==0:
#         sum += a
#         li.append(a)
#         a += 1
#     print(a, end = " ")
#     a += 1
# print("\n", li)
# print("5 배수의 합계 : ",sum)
