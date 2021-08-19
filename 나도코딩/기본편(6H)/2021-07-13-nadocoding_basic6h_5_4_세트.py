# ----------------------------------------------------------
# 집합 (set)
# - 중복이 되지 않다.
# - 순서가 없다.

my_set = {1, 2, 3, 3, 3}
print(my_set)  # 출력값 : {1, 2, 3}, 중복값 제거

# 개발자 set
# - {}
# - set([])

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))
# > 출력값 : {'유재석'}

# 합집합 (java 또는 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))
# > 출력값 : {'김태호', '유재석', '양세형', '박명수'}

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))
# > 출력값 : {'양세형', '김태호'}

# '김태호'가 python을 하게 되었다고 가정
python.add("김태호")
print(python)
# > 출력값 : {'유재석', '박명수', '김태호'}

# '김태호'가 java를 잊었다고 가정
java.remove("김태호")
print(java)
# > 출력값 : {'유재석', '양세형'}


#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
