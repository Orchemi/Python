# ----------------------------------------------------------
# Quiz 5
'''
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle 과 sample 을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)  # shuffle(lst) : lst 속 개체의 순서를 섞겠다.
print(lst)
print(sample(lst,1))  # sample(lst,n) : lst에서 sample로 n개만큼 뽑겠다.
'''


# 나의 작성 코드

from random import *
comment = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(comment)

chicken = comment[0]
coffee = comment [1:4]

print("-- 당첨자 발표 --\n치킨 당첨자 : " + str(chicken) + "\n커피 당첨자 : " + str(coffee))


# 모범 답안

from random import *
# users = [1, 2, 3, 4,...100]
users = range(1, 21)  # 1부터 20까지 숫자를 생성
print(type(users))  # 출력값 : <class 'range'>

users = list(users)  # class를 list로 변경
print(type(users))  # 출력값 : <class 'list'>

print(users)
shuffle(users)
print(users)

# 중복 당첨을 피하기 위해 한 번에 4명을 뽑는다.
winners = sample(users, 4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:4]))
print(" -- 축하합니다 -- ")



#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
