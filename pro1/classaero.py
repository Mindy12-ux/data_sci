class Sensor:

    def __init__(self, name, value):
        self.name =name
        self.value = value

    def measure(self):

        return f"{self.name} : {self.value}"



class OnboardComputer:

    def __init__(self):

        self.sensors = [
            Sensor("온도 센서", 24.5),
            Sensor("압력 센서", 101.3),
            Sensor("방사선 센서", 0.02)
        ]


    def check_sensors(self):
        for sensor in self.sensors:
            print(sensor.measure())

    # 연료 센서 추가 메소드 생성
    def fuelSensor(self, name, value):
        self.name = name
        self.value = value
        self.sensors.append(Sensor(self.name, self.value))

    # 센서명을 입력받아 객체를 반환하는 메소드 추가, self.sensor 리스트의 객체구조 이해하기 
    def get_sensor(self,name):

        for sensor in self.sensors:
            if sensor.name == name:
                return sensor

        return None
        



class Spacecraft:
    def __init__(self, name):
        self.name = name
        self.computer = OnboardComputer()

        #새로운 멤버 추가
        self.mission_name = "지구 관측"
        self.fuel_ = self.computer.get_sensor("연료량")

    def status(self):
        print(f"우주선 [{self.name}] 상태")
        self.computer.check_sensors()

    # 우주선 정보 추가
    def mission_info(self):
        print(f"우주선 : {self.name} \
                임무 : {self.mission_name}\
                연료량 : {self.fuel_}", sep="")



spacecraft = Spacecraft("아리랑-1")
spacecraft.computer.fuelSensor("연료량", "82.5%")
spacecraft.status()
print("---------------")
spacecraft.mission_info()