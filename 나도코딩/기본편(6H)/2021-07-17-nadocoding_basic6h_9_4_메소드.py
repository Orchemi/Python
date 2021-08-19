# ----------------------------------------------------------

# 메소드(Method)
## class의 정의

### 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

### 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
              # class 내 자기 자신에 대한 값을 호출하여 적용하는 것 self.~~
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage) )
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)

# firebat1이 5시 방향을 공격
firebat1.attack("5시")
# 출력값 : 파이어뱃 : 5시 방향으로 적군을 공격합니다. [공격력 : 16]

# firebat1이 25 데이지의 공격을 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)
# 출력값 :
# 파이어뱃 : 25 데미지를 입었습니다.
# 파이어뱃 : 현재 체력은 25 입니다.
# 파이어뱃 : 25 데미지를 입었습니다.
# 파이어뱃 : 현재 체력은 0 입니다.
# 파이어뱃 : 파괴되었습니다.



#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
