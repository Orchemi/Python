# ----------------------------------------------------------
# 패키지(Package)
#   모듈들을 모아놓은 집합
#   하나에 디렉토리에 여러 모듈 파일들을 모아놓은 것

# package 명 : travel
# module 명 : thailand, vietnam


# thailand.py 내용
"""
class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")
"""


# vietnam.py 내용
"""
class VietnamPackage:
    def detail(self):
        print("[베트남 패키지 3박 5일] 다낭 효도 여행 60만원")
"""


# package의 사용
#   travel package 내 thailand.py의 ThailandPackage class의 detail() 함수 사용
#   ※ import를 쓸 때 맨 뒤에는 모듈이나 패키지만 가능 / 클래스나 함수는 바로 import 불가능

import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
# 출력값 : [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원


# 함수/클래스의 호출
#   from ~~ import ~~ 의 끝에는 함수/클래스가 와도 된다.
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()







#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
