# 우편번호 파일 자료 읽기
# 키보드에서 입력한 동이름으로 해당 주소 정보 출력

def zipProcess():
    dongname = input("동 이름 입력 : ")
    #dongname = "명륜3가"
    #print(dongname)

    with open(r"zipcode.txt", mode="r", encoding="utf-8") as f:
        line = f.readline()
        print(line)
        #lines = line.split("\t")  # 문자열은 tab으로 구분되어 있다 ,['135-806', '서울', '강남구', '개포1동 경남아파트', '', '1\n']
        #lines = line.split(chr(9))  # tab에 해당하는  ascii 코드값(10진수), 위와 동일한 결과
        #print(lines)

        while line:     # 읽을 자료가 있으면 True, 읽을 자료가 없으면 False
            lines = line.split(chr(9))
            if lines[3].startswith(dongname):    #startswith()
                #print(lines)
                print(f"우 : {lines[0]} / {lines[1]} / {lines[2]} / {lines[3]}")

            line = f.readline()





if __name__ == "__main__":
    zipProcess()