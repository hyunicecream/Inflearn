#######################
####### 메소드 #########
#######################

# 일반 유닛
class Unit:
    def __init__(self, name, hp): #__init__ : 생성자 
        self.name = name
        self.hp = hp

# 공격유닛
class AttackUnit(Unit): # 일반유닛 ()상속 받고 싶은 클래스 입력
    def __init__(self, name, hp, damage): #__init__ : 생성자 
        Unit.__init__(self, name, hp)  # 생성자 호출      
        self.damage = damage        
    
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
