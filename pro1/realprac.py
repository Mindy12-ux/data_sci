def make_login_checker(max_attempts):
    fail_count_dic = {

    } 

    def fail_counter(name, status):
        if name not in fail_count_dic:

            fail_count_dic[name] = 0
        
        if status == False and fail_count_dic[name] < max_attempts:
            fail_count_dic[name] += 1

            return f"{name} : 로그인 실패 ({fail_count_dic[name]} / 3)"

        elif status == True and fail_count_dic[name] == max_attempts:
                    return f"{name} : 이미 잠긴 계정입니다."


        elif fail_count_dic[name] == max_attempts:
            return f"{name} : 계정이 잠겼습니다."

    
        else:
            return f"{name} : 로그인 성공!"

    return fail_counter

login_checker_cul = make_login_checker(3)
print(login_checker_cul("철수", False))
print(login_checker_cul("철수", False))
print(login_checker_cul("철수", False))
print(login_checker_cul("철수", False))
print(login_checker_cul("철수", True))
login_checker_youn = make_login_checker(3)
print(login_checker_youn("영희",True))