# ----------------------------------------------------------

# 멤버 변수의 사용
## 새 유닛의 생성 : Wraith

class Unit:
        def __init__(self, name, hp, damage):
            self.name = name
            self.hp = hp
            self.damage = damage
            print("{0} 유닛이 생성되었습니다.".format(self.name))
            print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않는다.)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 출력값 :
# 유닛 이름 : 레이스, 공격력 : 5


# 다크아칸의 mind control : 상대방 unit을 내 것으로 만드는 것
wraith2 = Unit("빼앗은 레이스", 80, 5)

# wraith2에는 clocking이라는 기능이 생겼다고 가정
# wraith2에 .clocking이라는 변수를 추가로 할당하는 것
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))




#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
