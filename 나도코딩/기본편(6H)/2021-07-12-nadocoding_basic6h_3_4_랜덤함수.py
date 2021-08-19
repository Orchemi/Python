# ----------------------------------------------------------
# 랜덤 함수
#   0.0 에서 1.0 사이에서 무작위로 숫자를 뽑아주는 것
from random import *

print(random())  # 0 ~ 1 미만의 임의의 실수 생성
print(random() * 10)  # 0 ~ 10 미만의 임의의 실수 생성
print(int(random()) * 10)  # 0 ~ 10 미만의 임의의 정수 생성


# 로또에 응용하기
print(int(random() * 45 + 1))  # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45 + 1))  # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45 + 1))  # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45 + 1))  # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45 + 1))  # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45 + 1))  # 1 ~ 45 이하의 임의의 값 생성


print(randrange(1, 46))  # 1 ~ 45 미만의 임의의 정수 생성
print(randint(1, 45))  # 양 끝의 값을 모두 포함하는 임의의 정수 생성



#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
