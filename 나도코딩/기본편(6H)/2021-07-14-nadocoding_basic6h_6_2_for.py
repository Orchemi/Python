# ----------------------------------------------------------
# for
#   식당에 손님이 많이 대기하는 상황

"""
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4") ...
"""


# 반복해서 칠 수 없을만큼 많은 경우

for waiting_no in [1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5):  # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 5):  # 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))


# 손님의 이름이 정해진 경우
starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다".format(customer))



#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
