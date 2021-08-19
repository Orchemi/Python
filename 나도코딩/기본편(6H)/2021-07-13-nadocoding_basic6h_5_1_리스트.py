# ----------------------------------------------------------
# 리스트 []

# 가정 1. 지하철 칸별로 10명, 20명, 30명이 있다고 가정
subway1 = 10
subway2 = 20
subway3 = 30

# 이는 다음과 같다.
subway = [10, 20, 30]

# 출력을 해보자.
print(subway)


# 가정 2. subway에 다음과 같은 문자열을 지정한다고 가정
subway = ["유재석", "박명수", "조세호"]
print(subway)  # 출력값 : ['유재석', '박명수', '조세호']

# 조세호는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))  # 0, 1, 2 이므로 2번째

# 다음 정류장에서 '하하'가 탄다고 가정
subway.append("하하")  # append : 리스트 추가 함수(맨 뒤에 추가)
print(subway)

# '정형돈'을 '박명수'와 '조세호' 사이에 넣는다고 가정
subway.insert(2, "정형돈")  # index : 2 의 위치에 넣는다.
print(subway)  # ['유재석', '박명수', '정형돈', '조세호', '하하']

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
# pop : list의 맨 뒤에서 한 개체를 꺼냄
# list의 맨 뒤인 '하하' 출력
print(subway)  # pop된 개체를 제외한 list 출력 ['유재석', '박명수', '정형돈', '조세호']


# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")  # 유재석을 list에 또 한 번 추가
print(subway)
print(subway.count("유재석"))  # list에서 "유재석" 의 개수 출력


# 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()  # .sort : 정렬한다는 함수
print(num_list)  # 출력값 : [1, 2, 3, 4, 5]


# 순서 뒤집기
num_list = [1, 2, 4, 3, 5]
num_list.reverse()  # .reverse : 리스트의 순서를 점점 작게 배치
print(num_list)  # 출력값 : [5, 4, 3, 2, 1]


# 모두 지우기
num_list = [1, 2, 3, 4, 5]
num_list.clear()  # .clear : 리스트 내의 개체를 모두 제거
print(num_list)  # 출력값 : [], 비어있는 리스트


# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]  # 문자형, 숫자형, Boolean형
print(mix_list)  # 출력값 : ['조세호', 20, True]


# 리스트 확장
num_list = [1, 2, 3, 4, 5]
mix_list = ["조세호", 20, True]

num_list.extend(mix_list)  # .extend : num_list 에 mix_list 붙여 확장
print(num_list)  # 출력값 : [1, 2, 3, 4, 5, '조세호', 20, True]




#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
