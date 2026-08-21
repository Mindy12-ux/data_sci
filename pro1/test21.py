class Info:
    

    def __init__(self, li):

        self.name = li[0]
        #self.birth = li[1]

    def showData(self):
        info = self.name #+ " " +str(self.birth)

        return info


me = Info(li= [input("이름을 입력하세요")])
print("고객님의 이름은 :", me.showData())
print(me.name)