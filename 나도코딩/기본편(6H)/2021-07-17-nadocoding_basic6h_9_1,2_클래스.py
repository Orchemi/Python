# ----------------------------------------------------------
# 클래스
#   스타크래프트 게임을 예시로 들겠다.

## 상황 1. 마린 1개, 탱크 1개
# 마린 : 공격 유닛, 군인, 총을 사용
name = "마린"  # 유닛의 이름
hp = 40  # 유닛의 체력
damage = 5  # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 출력값 :
# 마린 유닛이 생성되었습니다.
# 체력 40, 공격력 5


# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있다. 일반 모드 / 시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# 출력값 :
# 탱크 유닛이 생성되었습니다.
# 체력 150, 공격력 35


# 공격하는 상황
def attack(name, location, damage):
    # name : 어느 유닛이
    # location : 어느 위치로
    # damage : 얼마만큼의 피해를 줄지

    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
        .format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 출력값 :
# 마린 : 1시 방향으로 적군을 공격합니다. [공격력 5]
# 탱크 : 1시 방향으로 적군을 공격합니다. [공격력 35]



## 상황 2. 마린 1개, 탱크 2개

# 마린
name = "마린"
hp = 40
damage = 5

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))


# 탱크 1
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


# 탱크 2
tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 문제점 : 실제 게임에서는 탱크가 수십 개인데 매번 만들어주는 것은 무리이다.



## 상황 3. n개의 유닛에 대응하기
# class의 사용

class Unit:
        def __init__(self, name, hp, damage):
            self.name = name
            self.hp = hp
            self.damage = damage
            print("{0} 유닛이 생성되었습니다.".format(self.name))
            print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# __init__(self, name, hp, damage)에서 self를 제외한 나머지를 적는다.
# Unit(name, hp, damage)

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)

# 출력값 :
# 마린 유닛이 생성되었습니다.
# 체력 40, 공격력 5
# 마린 유닛이 생성되었습니다.
# 체력 40, 공격력 5
# 탱크 유닛이 생성되었습니다.
# 체력 150, 공격력 35



## __init 함수
#   python에서 쓰이는 생성자
#   class로부터 만들어지는 '객체'들이 만들어질 때 자동으로 호출
#   marine과 tank는 Unit class의 'instance'라고 표현
#   instance가 생성될 때에는 __init__ 함수의 정의된 개수와 동일하게 정의되어야 한다(self 제외)

"""
ex)
marine3 = Unit("마린")
marine3 = Unit("마린", 40)
사용 불가능!
"""


#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
