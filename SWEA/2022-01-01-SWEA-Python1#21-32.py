# 연습문제 1
scores = [88, 30, 61, 55, 95]
i = 1

while i <= 5:

    if scores[i-1] >= 60:
        print("{0}번 학생은 {1}점으로 합격입니다.".format(i, scores[i-1]))
        i += 1
    else:
        print("{0}번 학생은 {1}점으로 불합격입니다.".format(i, scores[i-1]))
        i += 1


# 연습문제 2
for i in range(1, 101):
    print(i)


# 연습문제 3
result = ""

for i in range(1, 101):
    if i % 2 == 0:
        result += "%d " % i

print(result[0:len(result)-1])


# 연습문제 4
result = ""

for i in range(1, 101):
    if i % 2 == 1:
        result += "%d, " % i

print(result[0: len(result) - 2])


# 연습문제 5
total = 0

for i in range(1, 100):
    if i % 3 == 0:
        total += i

print("1부터 100사이의 숫자 중 3의 배수의 총합: {}".format(total))


# 연습문제 6
blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
num_A, num_O, num_B, num_AB = 0, 0, 0, 0

for i in blood_type:

    if i == 'A':
        num_A += 1
    elif i == 'O':
        num_O += 1
    elif i == 'B':
        num_B += 1
    elif i == 'AB':
        num_AB += 1

result = {'A': num_A, 'O': num_O, 'B': num_B, 'AB': num_AB}
print(result)


# 연습문제 7
scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
i = 0
total = 0

while len(scores) >= 1:
    if scores[len(scores)-1] >= 80:
        total += scores[len(scores)-1]
    scores.pop()

print(total)


# 연습문제 8
i = 5

while i >= 1:
    print("*" * i)
    i -= 1


# 연습문제 9
star = 7
space = 0

while star >= 0:
    print("{0}{1}".format(" " * space, "*" * star))
    space += 1
    star -= 2


# 연습문제 10
num = input()
n0, n1, n2, n3, n4, n5, n6, n7, n8, n9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

for i in num:
    i_n = int(i)

    if i_n == 0:
        n0 += 1
    elif i_n == 1:
        n1 += 1
    elif i_n == 2:
        n2 += 1
    elif i_n == 3:
        n3 += 1
    elif i_n == 4:
        n4 += 1
    elif i_n == 5:
        n5 += 1
    elif i_n == 6:
        n6 += 1
    elif i_n == 7:
        n7 += 1
    elif i_n == 8:
        n8 += 1
    elif i_n == 9:
        n9 += 1

print("0 1 2 3 4 5 6 7 8 9")
print("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(
    n0, n1, n2, n3, n4, n5, n6, n7, n8, n9))


# 연습문제 11
for i in range(1, 6):
    print("{0:>5}".format("*" * i))


# 연습문제 13-A
d = int(input())

print("{0:b}".format(d))


# 연습문제 13-B
d = int(input())
result = ""
result_r = ""

while d > 0:
    a = d % 2
    result += "%d" % a
    d //= 2

print(result)

for i in range(1, len(result) + 1):
    result_r += result[len(str(result)) - i]

print(result_r)
