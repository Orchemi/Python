# ----------------------------------------------------------

# 예외처리
#   에러가 발생했을 때 그에 대해 처리를 해주는 것

print("나누기 전용 계산기입니다.")
num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))

print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))


## 상황 1. num1 = 6, num2 = 3 대입

# 출력결과는 다음과 같다.
"""
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 3
6 / 3 = 2
"""


## 상황 2. ValueError
#   num1 = 6, num2 = "삼" 대입

# 출력결과는 다음과 같다.
"""
ValueError: invalid literal for int() with base 10: '삼'
"""


## 상황 3. 해결책 'try'
#   try 내부의 구문을 실행하다가 오류가 발생한 경우, except를 찾는다.
#   except에 있는 error인 경우 error에 대한 내부 구문을 실행한다.

try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")


## 상황 4. ValueError 해결

# 출력결과는 다음과 같다.
"""
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 6
두 번째 숫자를 입력하세요 : 삼
에러! 잘못된 값을 입력하였습니다.
"""


## 상황 5. ZeroDivisionError
#   num1 = 6, num2 = 0 대입

# 출력결과는 다음과 같다.
"""
ZeroDivisionError: division by zero
"""


## 상황 6. ZeroDivisionError 해결

try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)

# num1 = 6, num2 = 0 대입한 후 출력한 결과는 다음과 같다.
"""
division by zero
"""


## 상황 7. IndexError
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)

# 출력결과는 다음과 같다.
"""
IndexError: list index out of range
"""


## 상황 8. IndexError 해결
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except:
    print("알 수 없는 에러가 발생하였습니다.")

# 출력결과는 다음과 같다.
"""
알 수 없는 에러가 발생하였습니다.
"""

#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
