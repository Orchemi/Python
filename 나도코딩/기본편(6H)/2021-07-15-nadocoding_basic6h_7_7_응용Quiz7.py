# ----------------------------------------------------------
# Quiz 7

## 문제
"""
Quiz) 표준 체중을 구하는 프로그램을 작성하시오.

* 표준체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
 남자 : 키(m) x 키(m) x 22
 여자 : 키(m) x 키(m) x 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)

조건 2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""

## 나의 작성 코드
from math import *

def std_weight(height, gender):
    if height >= 3:  # centimeter

        if gender == "남자":
            std_weight = (height/100)**2*22

        elif gender == "여자":
            std_weight = (height/100)**2*21

    else:           # meter

        if gender == "남자":
            std_weight = height**2*22
            height *= 100

        elif gender == "여자":
            std_weight = height**2*21
            height *= 100

    print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(round(height), gender, round(std_weight, 2)))


std_weight(174, "남자")


## 모범 답안

def std_weight(height, gender):  # 키는 meter 단위 고정(실수), 성별 "남자"/"여자"
    if gender == "남자":
        return height * height * 22
    else :
        return height * height * 21

height = 175  # centimeter 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))




#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
