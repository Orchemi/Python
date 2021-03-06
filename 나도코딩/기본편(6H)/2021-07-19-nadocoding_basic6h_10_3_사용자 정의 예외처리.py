# ----------------------------------------------------------
# 사용자 정의 예외처리
#   python에서 지정된 error가 아닌, 직접 정의한 error에 대해 처리하는 방법

class BigNumberError(Exception):
    pass

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")


## 상황 1. num1 = 10, num2 = 5

# 실행결과는 다음과 같다.
"""
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 10
두 번째 숫자를 입력하세요 : 5
에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
"""

## 상황 2
#   Error 발생시 메세지를 같이 넣고 싶은 경우
#   메세지 : [입력값 : num1, num2]

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)

# 출력결과는 다음과 같다.
"""
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 10
두 번째 숫자를 입력하세요 : 5
에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
입력값 : 10, 5
"""




#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
