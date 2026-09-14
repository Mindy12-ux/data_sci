year = int(input("연도 입력 : "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}은 윤년")

else:
    print(f"{year}은 평년")