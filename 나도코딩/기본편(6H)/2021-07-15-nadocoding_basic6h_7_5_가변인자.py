# ----------------------------------------------------------
# 가변인자를 이용한 함수 호출

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}".format(name, age), end=" ")
    # , end=" " -> 함수가 끝나고 출력시 줄바꿈을 하고 싶지 않을 때 사용

    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# 출력값 :
# 유재석 20 Python Java C C++ C#
# 김태호 25 Kotlin Swift

# 문제점 1 : 이후 작성에서도 사용 언어가 5개 미만인 경우 계속 "" 변수에 넣어주어야 한다.
# 문제점 2 : 유재석이 사용할 수 있는 언어가 1개 늘어날 경우, 함수 자체를 바꿔야한다.


# 해결방법 : 가변인자 사용
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()     # 줄바꿈을 위한 코드

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

# 출력값 :
# 이름 : 유재석	나이 : 20 Python Java C C++ C# JavaScript
# 이름 : 김태호	나이 : 25 Kotlin Swift



#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
