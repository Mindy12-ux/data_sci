# 리스트를 통해 직원 자료를 입력받아 가공 후 출력하기
# 급여액 = myPay, 기본급 = pay, 근속수당 = gun, 공제액 = gong, 수령액 = totPay


# 급여액 정의

mypay = 0

# 직원 데이터 입력

def inpufunc():
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005]
    ]
    return datas


# 급여 처리
def processfunc(datas):
    print("사번   이름   기본급   근무년수   근속수당    공제액   수령액")
    print("-------------------------------------------------------")

    #각 사원들의 근무년수, 근속 수당, 공제액, 수령액을 각각 담아놓을 리스트 생성
    year_li = []
    sudan_li = []
    gongse_li = []
    su_li = []

    
    for num in range(len(datas)):
        # (현재 년수 - 입사년도)로 근무년수를 구하고 근무년수 리스트에 저장
        year_li.append(2026 - int(datas[num][3]))

        # 근속수당을 계산해 근속수당 리스트에 저장
        if 2026 - int(datas[num][3]) <= 3:
            sudan_li.append(150000)
        elif 3 < 2026 - int(datas[num][3]) <=8:
            sudan_li.append(450000)
        else:
            sudan_li.append(1000000)

        # 급여액 계산
        mypay = int(datas[num][2]) + int(sudan_li[num])

        # 공제율을 계산해서 공제율 리스트에 저장
        if mypay <2000000:
            gongse_li.append(mypay * 0.15)
        elif 2000000 <= mypay < 3000000:
            gongse_li.append(mypay * 0.3)
        else:
            gongse_li.append(mypay * 0.5)

    # print(year_li)
    # print(sudan_li)
    # print(gongse_li)

    # 수령액 계산해서 리스트에 저장
    for i in range(len(datas)):
        # 수령액 계산해서 리스트에 저장
        su_li.append(int(datas[i][2]) + sudan_li[i] - gongse_li[i])

        # 각 리스트에서 요소를 추출해 출력
        for j in range(3):
            print(f"{datas[i][j]}", end = "   ")
        print(f"{year_li[i]}  {sudan_li[i]}  {gongse_li[i]}  {su_li[i]}")    
    print(f"처리 건수 : {len(datas)} 건")
    #{year_li[i]} {sudan_li[i]}  {gongse_li[i]}



processfunc(inpufunc())