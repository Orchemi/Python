# ----------------------------------------------------------

# 메소드 오버라이딩(Method Overriding)
#   부모 class에서 정의한 method 말고, 자식 class에서 새롭게 정의한 method를 사용하는 것


## 1. 기존 class

### 가. 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    # 지상 유닛의 이동
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
              .format(self.name, location, self.speed))


### 나. 공격 유닛
class AttackUnit(Unit):     # 상속 받고 싶은 class를 괄호에 넣어준다.
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)       # Unit class의 name, hp를 가져오는 코드
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


### 다. 공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]" \
              .format(name, location, self.flying_speed))


### 라. 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        # flying_speed가 있으므로 speed는 필요가 없어서 speed 자리에 0 입력

        Flyable.__init__(self, flying_speed)


## 2. 신규 유닛

### 가. 벌쳐 : 지상 유닛, 기동성이 좋다.
vulture = AttackUnit("벌쳐", 80, 10, 20)

### 나. 배틀크루저 : 공중 유닛, 체력, 공격력이 좋다.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

## 3. 적용
### 가. 상황 1
vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")

# 출력값 :
# 벌쳐 : 11시 방향으로 이동합니다. [속도 : 10]
# 배틀크루저 : 9시 방향으로 날아갑니다. [속도 : 3]

# 문제점 : 유닛을 움직이는 move 함수를 쓰는 것과 fly 함수를 쓸 때
# 지상 유닛과 공중유닛을 모두 구분해야 하기 때문에 번거롭다.
# 해결책 : FlyableAttackUnit class에 move 함수를 새롭게 define한다.


### 나. 상황 2
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        # flying_speed가 있으므로 speed는 필요가 없어서 speed 자리에 0 입력

        Flyable.__init__(self, flying_speed)

    # move 함수 새롭게 정의
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture.move("11시")
battlecruiser.move("9시")

# 출력값 :
# [지상 유닛 이동]
# 벌쳐 : 11시 방향으로 이동합니다. [속도 : 10]
# [공중 유닛 이동]
# 배틀크루저 : 9시 방향으로 날아갑니다. [속도 : 3]



#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
