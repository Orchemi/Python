# 연습문제 1-A    # 현재 연도를 가져오는 모듈 사용 : Fail
import datetime

dt = datetime.datetime.now()

thisYear = dt.year

name = input()
age = int(input())

print("{0}(은)는 {1}년에 100세가 될 것입니다.".format(name, thisYear + 100 - age))


# 연습문제 1-B  # 연도 2019년으로 하드코딩 : Pass
thisYear = 2019
name = input()
age = int(input())

print("{0}(은)는 {1}년에 100세가 될 것입니다.".format(name, thisYear + 100 - age))


# 연습문제 4
input = list(
    "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC")
result = 0

score_list = list(map(lambda x: 69 - ord(x), input))

for i in score_list:
    result += i

print(result)


# 연습문제 5
def Multiplication(*num):
    result = 1

    for i in num:
        if type(i) == int:
            result *= i
        else:
            result = "에러발생"
            break

    print(result)


Multiplication(1, 2, '4', 3)


# 연습문제 6
num = int(input())
print("ASCII {0} => {1}".format(num, chr(num)))


# 연습문제 7
lst = range(1, 11)
lst_even = list(filter(lambda x: x % 2 == 0, lst))

print(lst_even)


# 연습문제 8
lst = range(1, 11)
lst_square = list(map(lambda x: pow(x, 2), lst))

print(lst_square)


# 연습문제 9
lst = range(1, 11)
lst_f = list(filter(lambda x: x % 2 == 0, lst))
lst_fm = list(map(lambda x: pow(x, 2), lst_f))

print(lst_fm)


# 연습문제 10
def max(*params):
    max_num = 0

    for param in params:
        if param > max_num:
            max_num = param

    print("max{0} => {1}".format(params, max_num))


max(3, 5, 4, 1, 8, 10, 2)


# 연습문제 11
string_list = list("abcdef")

for idx, val in enumerate(string_list):
    print("{0}: {1}".format(val, idx))
