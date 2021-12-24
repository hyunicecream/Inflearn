class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flayable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self) # 초기화 방법
        Flyable.__init__(self) # 초기화 방법


