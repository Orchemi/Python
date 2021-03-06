# ----------------------------------------------------------

# 스타크래프트 프로젝트 전반전

## 0. 기본 설정
from random import *


## 1. 유닛 class

### 가. 일반 유닛
class Unit:

    # 유닛 초기화 및 생성 안내
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))

    # 지상 유닛의 이동
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]" \
              .format(self.name, location, self.speed))

    # 일반 유닛의 피해
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


### 나. 공격 유닛
class AttackUnit(Unit):

    # Unit class에서 상속 및 초기화, damage 추가
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)       # Unit class의 name, hp를 가져오는 코드
        self.damage = damage        # 일반 유닛에 추가로 damage를 적용

    # 공격 유닛이 공격하는 경우
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]" \
              # class 내 자기 자신에 대한 값을 호출하여 적용하는 것 self.~~
              .format(self.name, location, self.damage))

    # 공격 유닛이 공격 받는 경우
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


### 다. 공중 유닛
class Flyable:

    # 비행 속도 추가
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    # 비행 위치 안내
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]" \
              .format(name, location, self.flying_speed))


### 라. 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):

    # 공중 공격 유닛으로, 공격 유닛과 공중 유닛 상속 받은 것 초기화
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    # 공중 공격 유닛 비행 시, fly 함수 사용
    def move(self, location):
        self.fly(self.name, location)


## 2. 실제 Unit별 class 추가

### 가. 마린
class Marine(AttackUnit):

    # 공격 유닛 class 초기화 및 요소 입력
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 자기 체력 10 감소시켜 일정 시간동안 이동 및 공격 속도 증가
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다.".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용할 수 없습니다.". format(self.name))

### 나. 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가
    # 시즈모드 사용 시 모든 탱크에 적용되므로 class Tank 바로 밑에 지정

    seize_developed = False  # 시즈모드 개발여부


    # 공격 유닛 class 초기화 및 요소 입력
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    # 시즈모드 관련
    def set_seize_mode(self):

        # 현재 시즈모드가 개발되지 않았다면 아무 일도 없다.
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드가 개발된 상황에서,
        # 시즈모드가 아니라면 시즈모드로 전환
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        # 현재 시즈모드라면 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


### 다. 레이스
class Wraith(FlyableAttackUnit):

    # FlyableAttackUnit class를 상속받은 것을 초기화한 뒤, 레이스 정보 입력
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False  # 기본값 : 클로킹 모드 해제 상태

    # clocking 관련
    def clocking(self):

        # 클로킹 모드인 경우 모드 해제
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False

        # 클로킹 모드가 아닌 경우 모드 설정
        else:
            print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True


## 2. 게임 관련 함수
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")  # good game
    print("[Player]님이 게임에서 퇴장하셨습니다.")


## 3. 게임 진행

### 가. 게임 시작
game_start()


### 나. 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()


### 다. 탱크 2기 생성
t1 = Tank()
t2 = Tank()


### 라. 레이스 1기 생성
w1 = Wraith()


### 마. list로 유닛 일괄 관리
#   생성된 모든 유닛을 append로 추가
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)


### 바. 1시 방향으로 전군 이동
for unit in attack_units:
    unit.move("1시")


### 사. 탱크 시즈모드 개발
Tank_seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")


### 아. 공격 모드 준비
#   탱크 : 시즈모드 설정
#   레이스 : 클로킹 설정
#   마린 : 스팀팩 설정

#   isinstance : 해당 요소가 어떠한 class의 instance인지 확인

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()

    elif isinstance(unit, Tank):
        unit.set_seize_mode()

    elif isinstance(unit, Wraith):
        unit.clocking()


### 자. 전군 공격
for unit in attack_units:
    unit.attack("1시")


### 차. 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))  # 공격은 5~20 사이의 공격을 랜덤으로 받는다.


### 카. 게임 종료
game_over()





#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
