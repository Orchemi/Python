# ----------------------------------------------------------
# Finally
#   예외처리 구문에서 정상적으로 실행이되든, 오류가 발생하든, 무조건 정상적으로 실행되는 구문

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
finally:
    print("계산기를 이용해주셔서 감사합니다.")







#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
