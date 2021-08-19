# ----------------------------------------------------------

# 패스(Pass)
#   코드가 미완성이어도 오류 없이 다음 코드로 넘어가는 것

## 상황 1. 미완성 코드
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():

# 함수 호출
game_start()
game_over()

# 출력값 : 오류 발생
# game_start()
# ^
# IndentationError: expected an indented block


## 상황 2. Pass 사용
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

# 함수 호출
game_start()
game_over()

# 출력값 : [알림] 새로운 게임을 시작합니다.




#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
