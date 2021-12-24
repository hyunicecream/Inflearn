#######################
####### 멤버 변수 #######
#######################
#클래스 생성
class Unit:
    def __init__(self, name, hp, damage): #__init__ : 생성자 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # 클래스 사용방법, self를 제외한 개수 만큼 값을 입력해주어야 한다. 
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# #### 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음) #####
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 {1}".format(wraith1.name, wraith1.damage))

# #### 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음) #####
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{} 는 현재 클로킹 상태입니다.".format(wraith2.name))


# 공격유닛
class AttackUnit:
    def __init__(self, name, hp, damage): #__init__ : 생성자 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}])"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃: 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
