# ----------------------------------------------------------

# 상속

### 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

### 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

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


## 메딕 : 의무병, 공격력이 없음
#   일반 유닛과 공격 유닛 모두 name과 hp는 똑같은 내용이기 때문에 중복될 필요가 없다.
#   Unit class의 내용을 상속받아서 AttackUnit class에 적용하기 위함.

### 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

### 공격 유닛
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



#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
