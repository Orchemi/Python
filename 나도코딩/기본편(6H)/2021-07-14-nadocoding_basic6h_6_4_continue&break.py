# ----------------------------------------------------------
# continue와 break
#   선생님이 수업 중 출석번호로 학생들에게 책을 읽으라고 하는 경우 가정
#   출석번호 2, 5번은 결석
#   출석번호 7번은 책이 없다
#   continue : 출석번호 2, 5번은 skip하고 계속 책을 읽게 하는 역할

absent = [2, 5] # 결석
no_book = [7]  # 책이 없음

for student in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue              # 해당 student에 대한 코드 진행은 더 없이 다음 student에 대한 반복 진행
    elif student in no_book
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break                 # for문 반복 완전 종료
    print("{0}야, 책을 읽어봐.".format(student))






#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
