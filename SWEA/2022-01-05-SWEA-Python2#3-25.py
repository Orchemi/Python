# 연습문제 1
import math
lst = []

s1 = (90, 80)
lst.append(s1)

s2 = (85, 75)
lst.append(s2)

s3 = (90, 100)
lst.append(s3)

for i, val in enumerate(lst):
    total = 0
    avg = 0

    for j in val:
        total += j

    avg = total / len(val)

    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2:.1f}입니다.".format(i + 1, total, avg))


# 연습문제 2

target_text = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
target_list = list(target_text)

aeiou_text = 'aeiou'
aeiou_list = list(aeiou_text)

result_list = [item for item in target_list if not item in aeiou_list]
result_text = ""

for item in result_list:
    result_text += item

print(result_text)


# 연습문제 3

result_list = []

for a1 in range(2, 10):

    # 각 단에 필요한 내부 리스트를 초기화
    list_inner = []
    list_inner_f = []

    for a2 in range(1, 10):
        ggd_result = a1 * a2
        list_inner.append(ggd_result)

    # 필터링 전의 각 단의 결과들 리스트를 리스트 내포로 필터링
    list_inner_f = [item for item in list_inner if not (
        (item % 3 == 0) or (item % 7 == 0))]

    result_list.append(list_inner_f)

print(result_list)


# 연습문제 4
data_list = []
result = 0

for i in range(0, 5):
    a = int(input())
    data_list.append(a)

result_list = [item / len(data_list) for item in data_list]

result = sum(result_list)

print("입력된 값 {0}의 평균은 {1:.1f}입니다.".format(data_list, result))


# 연습문제 6
num = int(input())

result_list = [item for item in range(1, num + 1) if (num % item == 0)]

print(result_list)


# 연습문제 7
num = int(input())

result_list = [item for item in range(1, num + 1) if (num % item == 0)]
print(result_list)


# 연습문제 8
data_list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]

result_list = [item for item in data_list if (item % 2 == 0)]
print(result_list)


# 연습문제 11
def fibon(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fibon(x-2) + fibon(x-1)


a = 10
answer_list = [fibon(x) for x in range(a)]
print(answer_list)


# 연습문제 12

list_origin = list(range(1, 21))

result_list = [
    item ** 2 for item in list_origin if not ((item % 3 == 0) and (item % 5 == 0))]

print(result_list)


# 연습문제 13
data_list_str = list(input())
data_list_int = [int(item) for item in data_list_str]

print("{0}".format(sum(data_list_int)))


# 연습문제 14-A

dicBase = (('가', '깋'), ('나', '닣'), ('다', '딯'), ('라', '맇'), ('마', '밓'), ('바', '빟'), ('사', '싷'),
           ('아', '잏'), ('자', '짛'), ('차', '칳'), ('카', '킿'), ('타', '팋'), ('파', '핗'), ('하', '힣'))

inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다', '수출', '계시다', '다',
             '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그', '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이', '뜨겁다']


outer_list = []

for dic in dicBase:  # 외부 for문

    inner_list = []

    for target in inputWord:  # 내부 for문

        if dic[0] <= target <= dic[1]:
            inner_list.append(target)

    outer_list.append(inner_list)


# 연습문제 14-B
dicBase = (('가', '깋'), ('나', '닣'), ('다', '딯'), ('라', '맇'), ('마', '밓'), ('바', '빟'), ('사', '싷'),
           ('아', '잏'), ('자', '짛'), ('차', '칳'), ('카', '킿'), ('타', '팋'), ('파', '핗'), ('하', '힣'))

inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다', '수출', '계시다', '다',
             '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그', '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이', '뜨겁다']

outer_list = []

for dic in dicBase:
    inner_list = []
    inner_list = [target for target in inputWord if(
        dic[0] <= target <= dic[1])]

    outer_list.append(inner_list)

print(outer_list)


# 연습문제 16-A
txt = input()
list = []
element = ""

for i in txt:
    try:
        int(i)

    except:
        if i == ",":
            list.append(int(element))
            element = ""

    else:
        element += i

list.append(int(element))

tuple = tuple(list)

print(list)
print(tuple)


# 연습문제 16-B
a = input()
t_list = list(map(int, a.split(',')))
t_tuple = tuple(map(int, a.split(',')))

print(t_list)
print(t_tuple)


# 연습문제 17

input_txt = '2, 3, 4, 5'
result = ""

r_list = list(map(int, input_txt.split(', ')))
l_list = [2 * math.pi * r for r in r_list]

for l in l_list:
    result += "{0:.2f}, ".format(l)

print(result[:-2])


# 연습문제 18
input = list(map(int, input().split(', ')))
r = input[0]
c = input[1]

list_o = []
list_i = []

for i in range(0, r):
    list_i = []

    for j in range(0, c):
        list_i.append(j * i)

    list_o.append(list_i)

print(list_o)


# 연습문제 19
input = list(input().split(', '))
input_s = sorted(input)

result = ""

for i in input_s:
    result += i
    result += ", "

print(result[:-2])


# 연습문제 20
odd_list = []
result = ""

input_list = list(map(int, input().split(', ')))

odd_list = [item for item in input_list if (item % 2 == 1)]

for i in odd_list:
    result += str(i)
    result += ", "

print(result[:-2])


# 연습문제 21
tuple_input = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
idx_f = len(tuple_input)
idx_h = int(idx_f / 2)

print(tuple_input[:idx_h])
print(tuple_input[idx_h:])


# 연습문제 22
list_i = [5, 6, 77, 45, 22, 12, 24]

list_r = [item for item in list_i if (item % 2 == 1)]
print(list_r)


# 연습문제 23
list_i = [12, 24, 35, 70, 88, 120, 155]

list_r = [item for item in list_i if (list_i.index(item) % 2 == 1)]
print(list_r)


# 연습문제 24
a = [0 for i in range(4)]
b = [a for i in range(3)]
c = [b for i in range(2)]
print(c)


# 연습문제 25

list_i = [12, 24, 35, 70, 88, 120, 155]
no_k = [1, 5, 6]
no_i = list(map(lambda x: x - 1, no_k))

list_r = [item for item in list_i if not (list_i.index(item) in no_i)]
print(list_r)


# 연습문제 26
list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]

list_r = [item for item in list1 if (item in list2)]
print(list_r)


# 연습문제 27

def KillTwin(lst):
    print(sorted(list(set(lst))))


list_i = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

KillTwin(list_i)
