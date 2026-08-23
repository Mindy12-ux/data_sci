# 클래스는 새로운 타입을 만들어 자원을 공유하는 것이 그 목적이다.
# 데이터와 기능을 하나의 단위로 묶어 새로운 사용자 정의 타입을 만들고, 
# 객체마다 상태를 가지게 하거나 공통자원을 공유할 수 있다.
"""
class Singer:
    title_song = "아리랑"

    def sing(self):
        msg = "노래는"
        print(msg, self.title_song)
"""

# import test22singer
# bts = test22singer.Singer()

from test22singer import Singer  #외부 모듈의 멤버 로딩

bts = Singer()
bts.sing()

print(type(bts))

bts.title_song = "Stay for the night"
bts.co = "빅히트 엔터테인먼트"
bts.sing()
print("bts 소속사 : ", bts.co)

print("=======================")
ive = Singer()
ive.sing()
print(type(ive))
ive.co = "Starship"
print("ive 소속사 : ", ive.co)

print()
Singer.title_song = "긴 여름은 가고"
ive.sing()
bts.sing()

niceGroup = ive
niceGroup.sing()
print(niceGroup.co)