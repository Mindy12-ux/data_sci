# 한 개의 상품명과 가격은 문자열로 입력됨. 문자열 나누기 필요

# 데이터 작성 
def inputfunc():
    datas =[
        "새우깡, 15",
        "감자깡, 20",
        "양파깡, 10",
        "새우깡, 30",
        "감자깡, 25",
        "양파깡, 40",
        "새우깡, 40",
        "감자깡, 10",
        "양파깡, 35",
        "새우깡, 50",
        "감자깡, 60",
        "양파깡, 20",
    ]
    return datas

# 처리 함수 
def processfunc(datas):

    print("상품명   수량   단가   금액")
    print("--------------------------")

    #상품과 수량을 저장할 리스트 작성
    snack = []
    num =[]

    for i in range(len(datas)):
        # 정규표현식 사용, 문자/숫자만 남기기
        import re
        new_li = re.sub(r"[^가-힣\d]", '', datas[i])
        snack.append(new_li[0:3])
        num.append(new_li[3:])
    # print(snack)
    # print(num)
    
    #상품별 금액 매칭
    for i in range(len(snack)):
        if snack[i] == "새우깡":
            danga = 450
        elif snack[i] == "감자깡":
            danga = 300
        else:
            danga = 350

        print(f"{snack[i]}   {num[i]}    {danga}      {int(num[i])*danga}")

    


processfunc(inputfunc())

