# ----------------------------------------------------------
# 지역변수와 전역변수

## 지역변수
#   함수 내에서만 쓸 수 있는 것
#   함수가 호출되며 만들어졌다가 함수가 끝나면 사라지는 일시적인 변수


## 전역변수
#   프로그램 내에서 어디서든지 불러낼 수 있는 변수


## 예시 1 : 지역변수 사용 오류
gun = 10

def checkpoint(soldiers):  # 경계근무 나가는 군인들의 수
    gun = gun - soldiers  # 기존 총의 수에서 근무군인들의 수만큼 뺀 값
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)  # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

# 출력값 : UnboundLocalError: local variable 'gun' referenced before assignment
# 함수 내에서 gun이라는 변수가 할당(초기화)되지 않았는데 사용이 되었기 때문에 생기는 오류
# 함수 내에서 지역변수 gun의 값을 지정하여 초기화시켜주어야 한다.


## 예시 2 : 지역변수 값 설정

gun = 10

def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

# 출력값 :
# 전체 총 : 10                | 밖에 있는 gun의 값은 변하지 않았다.
# [함수 내] 남은 총 : 18       | 안에 있는 gun의 값에서 조작 후 출력하였다.
# 남은 총 : 10                | 밖에 있는 gun의 값은 변하지 않았다.


## 예시 3 : 전역변수의 사용
#   global 변수명 으로 사용
#   전역공간에 있는 변수값을 사용하겠다.

gun = 10

def checkpoint(soldiers):
    global gun  # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

# 출력값 :
# 전체 총 : 10
# [함수 내] 남은 총 : 8       | 전역변수의 값을 함수 내에서 사용하였다.
# 남은 총 : 8                | 전역변수의 값이 변하였다.

# 문제점 : 전역변수를 많이 쓰게 되면 코드 관리가 어려워진다.
#    -> 일반적으로 권장되는 방법은 아니다.

# 해결책 : 함수의 전달값으로 계산하고 반환값을 받아서 사용


## 예시 4 : 권장되는 방식

gun = 10

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun  # 함수 내에서 바뀐 변수값을 외부의 변수값에 적용

print("전체 총 : {0}".format(gun))

# 외부의 변수값이 함수를 호출하여 값을 재지정
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

# 출력값 :
# 전체 총 : 10
# [함수 내] 남은 총 : 8
# 남은 총 : 8

#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
