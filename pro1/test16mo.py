# 현재 모듈은 다른 package에 있는 모듈의 멤버를 사용해
# 실행을 통해 어떤 결과를 확인할 수 있는 실행파일
# 실행 파일은 > python 파일명.py  <==  이 파일은 main module

print("사용자 정의 모듈 작성 후 호출 연습 ---")

imsi = 100

print("\n경로 지정 방법1 : import 모듈명")
import pack1.mymod1
print(dir(pack1.mymod1))
print(pack1.mymod1.__file__)  # 경로명 및 파일명
print(pack1.mymod1.__name__)  # 모듈명

list1 = [1,2]
list2 = [3,4,5]

pack1.mymod1.listHap(list1, list2)
if __name__ == "__main__":
        print("와우 내가 모듈이야")  # 와우 내가 모듈이야, test15mo.py가 메인모듈임


print("\n경로 지정 방법2 : from 모듈명 import 모듈멤버, ... ")
from pack1.mymod1 import kbsFunc

kbsFunc()

from pack1.mymod1 import mbcFunc
from pack1.mymod1 import tot
mbcFunc()
print("tot :", tot)

from pack1.mymod1 import kbsFunc as 케이비에스별명
케이비에스별명()    # 대한민국 대표 방송

print("\n경로 지정 방법3 : import 하위패키지.모듈명")

import pack1.subpack.sbs
pack1.subpack.sbs.sbsManse()
import pack1.subpack.sbs as 난별명
난별명.sbsManse()

print()
from pack1_other import mymod2

imsi = mymod2.Hap(3,4)
print(imsi)

from pack1_other.mymod2 import Cha as chachacha
print(chachacha(5,2))

print("\n경로 지정 방법4 : path 설정이 된 폴더에 모듈이 저장된 경우")
# 예) C:\Users\acorn\anaconda3\envs\myproject\Lib에 저장

import mymod3   # import math, import datetimes 등 이미 경로에 저장된 파일이므로 경로 설정을 하지 않아도 호출할 수 있음
print(mymod3.Gop(4,5))

import numpy
print(numpy.array(1))

import mailbox
print(mailbox.Error("dlfslkdfjl3413"))

