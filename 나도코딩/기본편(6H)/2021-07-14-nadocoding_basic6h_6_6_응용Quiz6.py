# ----------------------------------------------------------
# Quiz
"""
당신은 Cocoa 서비스를 이용하는 택시기사입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
조건 2 : 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
"""


# 나의 작성 코드
index = 1
total = 0

from random import *

while index < 51:
    time = randint(5, 50)

    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(index, time))
        index += 1
        total += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(index, time))
        index += 1

print("\n총 탑승 승객 : " + str(total) + "분")


# 모범 답안
from random import *
cnt = 0  # 총 탐승 승객 수
for i in range(1, 51):  # 1 ~ 50의 난수 (승객)
    time = randrange(5, 51)  # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15:  # 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:  # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))


#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
