class Machine:
    volume = 0

#볼륨을 계속 조절하고 현재 볼륨이 얼마인지 보여줌, \
# 볼륨이 0일때와 50 이상일 때 경고 메세지 출력

    def volumeControl(self, volume):
        pass


class ElecRadio(Machine):

    def volumeControl(self, volume):
        self.volume += volume

        if self.volume <= 0:
            return f"현재 볼륨 : {self.volume}, 볼륨이 0입니다. 소리를 키워주세요"

        elif 0 < self.volume < 50:
            return f"현재 볼륨 : {self.volume}"

        elif 50 <= self.volume: 
            return f"현재 볼룸 : {self.volume}, 볼륨이 50 이상입니다. 소리를 낮춰주세요"


class ElecTv(Machine):

    volume_tv = 0

    def volumeControl(self, volume_remote = 0, volume_non_remote = 0):
        self.volume += volume_remote
        self.volume += volume_non_remote

        if self.volume <= 0:
            return f"현재 볼륨 : {self.volume}, 볼륨이 0입니다. 소리를 키워주세요"

        elif self.volume > 100:
            return f"현재 볼륨 : {self.volume}, 볼륨이 100 이상입니다. 소리를 낮춰주세요"

        else:
            return f"현재 볼륨 : {self.volume}"


radio = ElecRadio()

print(radio.volumeControl(10))
print(radio.volumeControl(50))


tv = ElecTv()
print(tv.volumeControl(50))
print(tv.volumeControl(100))
print(tv.volumeControl(10, -70))



print("------------다형성 2")

group = [ElecTv(), ElecRadio()]

for g in group:
    print(g.volumeControl(50))
    