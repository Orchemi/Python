# 연습문제 1
word = input()
result = ""

for i in word:
    result = i + result

print(result)

if word == result:
    print("입력하신 단어는 회문(Palindrome)입니다.")


# 연습문제 2

def 가위바위보(man1, man2):
    if man1 == man2:
        print("비겼습니다!")
    elif man1 == "가위":
        if man2 == "바위":
            print("바위가 이겼습니다!")
        elif man2 == "보":
            print("가위가 이겼습니다!")
    elif man1 == "바위":
        if man2 == "가위":
            print("바위가 이겼습니다!")
        elif man2 == "보":
            print("보가 이겼습니다!")
    elif man1 == "보":
        if man2 == "바위":
            print("보가 이겼습니다!")
        elif man2 == "가위":
            print("가위가 이겼습니다!")


player1 = input()
player2 = input()
man1 = input()
man2 = input()

가위바위보(man1, man2)


# 연습문제 3
num = int(input())


def IsPrimeNumber(number):
    cnt = 0

    for i in range(1, number + 1):
        if number % i == 0:
            cnt += 1

    if cnt == 2:
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")


IsPrimeNumber(num)


# 연습문제 4
a = 1
b = 0
c = 0
iteration = int(input())
lst = []

for i in range(0, iteration):
    c = a + b
    a = b
    b = c
    lst.append(c)

print(lst)


# 연습문제 5
lst_result = []
lst_target = [1, 2, 3, 4, 3, 2, 1]


def DuplicationRemove():
    for i in lst_target:
        if not (i in lst_result):
            lst_result.append(i)

    print(lst_result)


print(lst_target)
DuplicationRemove()


# 연습문제 6
num1 = 5
num2 = 10
lst = [2, 4, 6, 8, 10]


def IsInList(num):
    isIn = False

    for i in lst:
        if num == i:
            isIn = True
            break

    print(str(num) + " => " + str(isIn))


print(lst)
IsInList(num1)
IsInList(num2)


# 연습문제 7
num = int(input())


def Factorial(a):
    result = 1

    while a >= 1:
        result *= a
        a -= 1

    print(result)


Factorial(num)


# 연습문제 8

data = input()
data_list = data.split(", ")


def square(num):
    print("square({0}) => {1}".format(num, num ** 2))


for i in data_list:
    i_num = int(i)
    square(i_num)


# 연습문제 9
data = input()
data_list = data.split(", ")


def LongString(lst):

    max_length = 0
    temp = ""

    for i in lst:
        if max_length < len(i):
            max_length = len(i)
            temp = i

    print(temp)


LongString(data_list)


# 연습문제 10

def countdown(sec):
    if sec <= 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        while sec >= 1:
            print(sec)
            sec -= 1


countdown(0)
countdown(10)
