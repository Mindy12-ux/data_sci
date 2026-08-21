def inputfunc():
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005],
    ]
    return datas

def processfunc(datas):

    import datetime

    curr_year = datetime.datetime.now().year

    for data in datas:

        num, name, base_pay, woking_year = data

        #calculate bonus
        if (curr_year - woking_year) <= 3:
            bonus = 150000

        elif  3 < (curr_year - woking_year) <=8:
            bonus = 450000

        else:
            bonus = 1000000


        #calculate tax rate
        if (base_pay + bonus) < 2000000:
            rate = 0.15
        elif 2000000 <= (base_pay + bonus) < 3000000:
            rate = 0.3

        else:
            rate = 0.5

        net_pay = (base_pay + bonus) - (base_pay + bonus) * rate

        data.extend([curr_year-woking_year, bonus, (base_pay + bonus) * rate, net_pay])

    print(datas)

    print("사번    이름    기본급    근무년수    근속수당    공제액    수령액")
    print("-"*70)


    for data in datas:
        print(
            f"{data[0]}",
            f"{data[1]}",
            f"{data[2]}",
            f"{data[4]}",
            f"{data[5]}",
            f"{data[6]}", 
            sep = "    "
        )
    print("처리 건수 : ", len(datas))
processfunc(inputfunc())