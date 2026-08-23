def make_login_checker(max_attempts):
    total_fail = 0

    def fail_counter(name, status):
        nonlocal total_fail

        if status == False and total_fail < max_attempts:
             
            total_fail += 1

            return f"{name} : 로그인 실패 ({total_fail} / 3)"

        elif total_fail == max_attempts:
            return f"{name} : 계정이 잠겼습니다."

        else:
            return f"{name} : 로그인 성공!"


    return fail_counter

login_checker_cul = make_login_checker(3)
print(login_checker_cul("철수", False))
print(login_checker_cul("철수", False))
print(login_checker_cul("철수", False))
print(login_checker_cul("철수", False))
login_checker_youn = make_login_checker(3)
print(login_checker_youn("영희",True))