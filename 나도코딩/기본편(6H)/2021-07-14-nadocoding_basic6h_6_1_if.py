# ----------------------------------------------------------
# if
#   날씨에 따라서 서로 다른 실행을 하는 경우

"""
if 조건:
    실행 명령문
"""

weather = "비"
if weather == "비":
    print("우산을 챙기세요")  # 출력값 : 우산을 챙기세요

if weather == "맑음":
    print("우산을 챙기세요")  # 출력값 : '' 없음


# elif의 활용
weather = "미세먼지"
if weather == "비":              # 상황 1
    print("우산을 챙기세요")
elif weather == "미세먼지":       # 상황 2
    print("마스크를 챙기세요")
else:                           # 그 외 상황
    print("준비물이 필요 없어요")

# 출력값 : 마스크를 챙기세요



# or/and의 활용
weather = "눈"
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
# 출력값 : 우산을 챙기세요


weather = "눈"
if weather == "비" and weather == "눈":
    print("우산을 챙기세요")
# 출력값 : '' 없음



# input의 활용
weather = input("오늘 날씨는 어때요? ")
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")


# input과 문자열
#   input은 항상 문자열로 값을 받으므로 숫자형으로 바꾸기 위해 int(input()) 사용

temp = int(input("기온은 어때요? "))
if temp >= 30:
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요.")


#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
