# ----------------------------------------------------------

# 슈퍼(Super)
#   다중 상속 상황에서 사용에 주의

## 1. 기존 class의 단순화 및 드랍쉽 생성
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

# 드랍쉽 생성 : 공중 유닛, 공격 X
dropship = FlyableUnit()

# 출력값 : Unit 생성자
# 즉, Unit 생성자는 __init__으로 초기화가 되었는데, Flyable 생성자는 초기화되지 않은 것.


## 2. FlyableUnit 상속 순서 변경
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()

# 드랍쉽 생성 : 공중 유닛, 공격 X
dropship = FlyableUnit()

# 출력값 : Flyable 생성자
# 2개 이상의 다중 속성을 받는 생성자의 경우, super을 쓰면 먼저 쓰인 class만 상속된다.
# 따라서 다중 상속을 하거나 모든 부모 class의 초기화가 필요하다면 따로 초기화를 명시하는 것이 필요하다.


## 3. 모든 부모 class 초기화
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽 생성 : 공중 유닛, 공격 X
dropship = FlyableUnit()

# 출력값 :
# Unit 생성자
# Flyable 생성자


#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
