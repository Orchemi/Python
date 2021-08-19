# ----------------------------------------------------------
# 튜플
# - 리스트와 달리 내용 변경/추가 불가능
# - 속도가 리스트보다 빠름
# -> 변경되지 않는 목록에 튜플을 사용

menu = ("돈까스", "치즈까스")  # 리스트 : {} / 튜플 : ()
print(menu[0])  # 출력값 : 돈까스
print(menu[1])  # 출력값 : 생선까스

# 튜플은 .add 기능을 지원하지 않는다.

menu.add("생선까스")
# 출력값 : AttributeError : 'tuple' object has no attribute 'add'


# 튜플의 활용
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)  # 출력값 : 김종국 20 코딩

# 이를 다음과 같이 한 번에 선언할 수 있다.
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)  # 출력값 : 김종국 20 코딩





#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
