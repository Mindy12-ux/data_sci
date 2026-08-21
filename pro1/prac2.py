def inputfunc():
    datas = [
        "새우깡,15",
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas

price_by_name = {
    "새우깡":450,
    "감자깡":300,
    "양파깡":350
}

print_list = []

def processfunc(datas):

    #make dictionary for name:price
    count_by_name = {name : 0 for name in price_by_name}
    amount_by_name = {name : 0 for name in price_by_name}

    for data in datas:
        name, count = data.split(",")
        count = int(count)
        count_by_name[name] += count
        amount_by_name[name] += count * price_by_name[name]




        print_list.append([name, count, price_by_name[name], count*price_by_name[name]])



    
    for data in print_list:
        print(
            f"{data[0]}",
            f"{data[1]}",
            f"{data[2]}",
            f"{data[3]}"

        )

    print("소계")

    for i in price_by_name:
        print(f"{i}  : {count_by_name[i]}  소계액 : {amount_by_name[i]}")

    print("총계")
    #print(f"총 건수 : {}")

processfunc(inputfunc())

