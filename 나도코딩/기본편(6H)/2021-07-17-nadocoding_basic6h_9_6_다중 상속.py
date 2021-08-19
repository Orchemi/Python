# ----------------------------------------------------------

# 다중 상속
#   부모 class를 2개 이상 상속 받는 것


## 1. 기존 class

### 가. 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

### 나. 공격 유닛
class AttackUnit(Unit):     # 상속 받고 싶은 class를 괄호에 넣어준다.
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)       # Unit class의 name, hp를 가져오는 코드
        self.damage = damage        # 일반 유닛에 추가로 damage를 적용

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]" \
              # class 내 자기 자신에 대한 값을 호출하여 적용하는 것 self.~~
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage) )
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


## 2. 신규 class

### 가. 공중 유닛 : 날 수 있는 기능을 가진 유닛

###    ex) 드랍쉽 : 공중유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격 X
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
              .format(name, location, self.flying_speed))


## 3. 다중 상속 적용 : 공중 공격 유닛 클래스
#   공격하는 AttackUnit, 날 수 있는 Flyable에서 모두 상속을 받아야 함
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

#   새로운 유닛, 발키리
#   공중공격 유닛, 한 번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
# 출력값 : 발키리 : 3시 방향으로 날아갑니다. [속도 : 5]


#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
