# 파일 읽기
with open("sales.txt", mode="r", encoding="utf-8") as f:
    # 한 줄씩 읽어오기
    line = f.readline()


    # total_list 리스트에 건수별로 각각의 총계 추가하기, imsi_saleman_name_list에 직원들 이름 추가

    total_list =[]
    imsi_saleman_name_list = []

    while line:

        # 한 행씩 "," 단위로 구분해서 건수의 개별 리스트 만들기
        lines = line.split(chr(44))

        # 총계 구하고 개별 리스트에 추가하기
        total_amount = int(lines[3]) * int(lines[4])
        lines.extend([total_amount])

        # saleman_name_list에 직원 이름 추가
        imsi_saleman_name_list.append(lines[1])

        # 개별 리스트를 total_list에 추가하기
        total_list.append(lines)

        line = f.readline()

    # set을 사용해 직원 이름 추출
    imsi = set(imsi_saleman_name_list)
    saleman_name_list = list(imsi)

    # total_per_saleman 딕셔너리를 생성해 직원별 판매액 저장
    total_per_saleman = {name : 0 for name in saleman_name_list}

    for i in total_list:
        total_per_saleman[i[1]] += i[5]

    print(total_per_saleman)  # {'김철수': 1350000, '이영희': 820000, '홍길동': 3450000}


    print("날짜            이름        상품명      갯수     판매금액")

    for i in total_list:
        print(f"{i[0]}      {i[1]}      {i[2]}      {i[3]}      {i[5]}")

    print(f"전체 판매 금액 : {sum(total_per_saleman.values())}원")
    print(f"판매왕 : {max(total_per_saleman.keys())}")
    


    file = open("sales_report.txt", mode="w", encoding="utf-8")
    file.write(f"직원별 판매 실적\n홍길동 : {total_per_saleman["홍길동"]}\n김철수 : \
    {total_per_saleman["김철수"]}\n이영희 : {total_per_saleman["이영희"]}\n\n전체 판매 금액 :\
    {sum(total_per_saleman.values())}\n판매왕 : {max(total_per_saleman.keys())} ({max(total_per_saleman.values())})원")

    










    