# ----------------------------------------------------------
# 모듈 직접 실행

## 가. 모듈 직접 실행
# thailand.py 파일을 다음과 같이 수정한다.
"""
class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행됩니다.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
"""

# 이후 thailand.py 에서 모듈을 실행하면 실행결과는 다음과 같다.
"""
Thailand 모듈을 직접 실행
이 문장은 모듈을 직접 실행할 때만 실행됩니다.
[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원
"""


## 나. 모듈 외부에서 호출
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 실행결과는 다음과 같다.
"""
Thailand 외부에서 모듈 호출
[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원
"""




#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
