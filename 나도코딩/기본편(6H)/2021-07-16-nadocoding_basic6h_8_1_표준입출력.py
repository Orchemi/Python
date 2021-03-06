# ----------------------------------------------------------
# 표준입출력

print("Python", "Java")
# 출력값 : Python Java

print("Python" + "Java")
# 출력값 : PythonJava


# sep(seperate)
#   문자열 연결을 어떻게 할지 지정

print("Python", "Java", sep=", ")
# 출력값 : Python, Java

print("Python", "Java", "JavaScript", sep=" vs ")
# 출력값 : Python vs Java vs JavaScript


# end
#   문장의 끝부분을 줄바꿈이 아니라, 다른 것으로 바꾸어 출력한다.

print("Python", "Java", sep=", ", end="?")
print("무엇이 더 재밌을까요?")
# 출력값 : Python, Java?무엇이 더 재밌을까요?
#   print문 두 개에서 나온 문장이 한 줄에 출력


# file
import sys  # sys 모듈 import
print("Python", "Java", file=sys.stdout)
# 출력값 : Python Java
#   표준 출력으로 문자 출력

print("Python", "Java", file=sys.stderr)
# 출력값 : Python Java
#   표준 에러로 처리

# 왜 필요한거지?


# dictionary
scores = {"수학":0, "영어":50, "코딩":100}  # dictionary
for subject, score in scores.items():    # .items() : key:value 쌍으로 tuple로 전달
    print(subject, score)
# 출력값 :
# 수학 0
# 영어 50
# 코딩 100


# just
#   tuple의 데이터를 정렬하고 싶을 때
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# l : left
# r : right
# 8 : 총 8칸의 공간을 만들고 왼쪽 정렬 후 출력해달라

# 출력값 :
# 수학      :   0
# 영어      :  50
# 코딩      : 100


# zfill(n)
#   n자리 만큼 공간을 만들고 값이 없는 빈 공간에 대해서는 0으로 출력
#   은행 대기순번표
#   001, 002, 003, ...

for num in range(1,21):
    print("대기번호 : " + str(num))

# 출력값 :
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# ...
# 대기번호 : 18
# 대기번호 : 19
# 대기번호 : 20

# 001, 002... 형식으로 앞에 빈 숫자를 두고 싶다면?
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))

# 출력값 :
# 대기번호 : 001
# 대기번호 : 002
# 대기번호 : 003
# ...
# 대기번호 : 018
# 대기번호 : 019
# 대기번호 : 020


# 표준입력
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")
print(type(answer))

# 입력값 : 10
# 출력값 :
# 입력하신 값은 10입니다.
# <class 'str'>

# 입력값 : Orchemi
# 출력값 :
# 입력하신 값은 Orchemi입니다.
# <class 'str'>

# 입력값이 숫자형이든, 문자형이든 input 함수를 통과하여 저장된 변수값은 모두 문자열(str) 형태로 저장





#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
