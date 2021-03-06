# ----------------------------------------------------------
# 문자열 처리 함수 -----------------------------------------------------------------------------------------
python = "Python is Amazing"  # 문자열 변수 지정

print(python.lower())  # python 변수의 값을 모두 소문자로 변환하여 출력
print(python.upper())  # python 변수의 값을 모두 대문자로 변환하여 출력
print(python[0].isupper())  # python 변수의 첫번째 값이 대문자인지의 여부
print(len(python))  # python 변수의 값의 길이, 즉 문자의 개수를 출력
print(python.replace("Python", "Java"))  # python 변수에서 Python 문자를 찾아서 Java로 바꾸기
print(python.count("n"))  # python 변수에서 "n"의 개수 파악, 2


# index 변수와 find 함수 -----------------------------------------------------------------------------------
index = python.index("n")  # python 변수 내에서 'n' 이라는 문자의 순서를 index 변수에 지정(숫자열), 5
print(index)

index = python.index("n", index + 1)  # index + 1 의 위치 이후의 다음 n을 찾아 해당 위치를 index 변수에 지정, 15
print(index)

print(python.find("n"))  # python 변수에서 n 문자를 찾는다, 5


# find 함수 vs index 변수 --------------------------------------------------------------------------------------
#   없는 값 "Java"를 python 변수에서 찾아보자.

print(python.find("Java"))
#   출력값 = -1 : 원하는 값이 없으면 -1 반환 -> 이후 코드 실행 O

print(python.index("Java"))
#   출력값 = ValueError : 오류를 내며 프로그램 종료 -> 이후 코드 실행 X





#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
