# ----------------------------------------------------------
# while
#   starbucks에서 5번이나 손님을 불렀는데 오지 않는 경우 커피를 버린다고 가정

"""
while (조건):
    실행문

# (조건)을 만족할 때까지 코드 실행
"""

# case 1. starbucks
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")



"""
# case 2. megacoffee
index = 1
customer = "아이언맨"

while True:
    print("{0}님, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
    index += 1
"""

#   출력 : 무한루프에 빠짐
#   무한루프에서 벗어나기 위해선 <ctrl + c>


# case 3. gongcha
#   손님들이 와서 커피가 준비되었는지 물을 때, 이름을 물어봐서 커피를 주는 경우

target = "토르"  # 커피가 준비된 사람
visitor = "Unknown"  # 종업원에게 찾아온 사람

while visitor != target:
    print("{0}님, 커피가 준비되었습니다".format(visitor))
    visitor = input("이름이 어떻게 되세요? ")

#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
