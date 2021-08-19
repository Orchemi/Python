# ----------------------------------------------------------
# 한 줄로 끝내는 for문 활용
"""
출석번호가 1, 2, 3, 4... 앞에 100을 붙이기로 가정
-> 101, 102, 103, 104
"""

students = [1,2,3,4,5]
print(students)  # 출력값 : [1, 2, 3, 4, 5]


# 출석번호에 100 더하기
students = [i+100 for i in students]
print(students)  # 출력값 : [101, 102, 103, 104, 105]


# 학생 이름을 길이로 변환
students = ["Ironman", "Thor", "Groot"]
students = [len(i) for i in students]
print(students)  # 출력값 : [7, 4, 5]


# 학생 이름을 대문자로 변환
students = ["Ironman", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students)




#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
