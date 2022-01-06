# 연습문제 2
students = {"홍길동": "010-1111-1111", "이순신": "010-1111-2222", "강감찬": "010-1111-3333"}

print("아래 학생들의 전화번호를 조회할 수 있습니다.")

for key in students.keys():
    print(key)

print("전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.")

target = input()

print("{0}의 전화번호는 {1}입니다.".format(target, students[target]))


# 연습문제 3-B
import operator

dic = {
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000,
}

dic = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
for key, value in dic.items():
    print("{0}: {1}".format(key, value))


# 연습문제 4
a = {
    "아메리카노": 1900,
    "카페모카": 3300,
    "에스프레소": 1900,
    "카페라떼": 2500,
    "카푸치노": 2500,
    "바닐라라떼": 2900,
}
b = {"헤이즐럿라떼": 2900, "카페모카": 3300, "밀크커피": 3300, "아메리카노": 1900, "샷크린티라떼": 3300}

b.update(a)

# for item in b.items():
#     if item[1] >= 3000:
#         print(item)

result = {item for item in b.items() if item[1] >= 3000}
print(result)


# 연습문제 5
fruit = [" apple ", "banana", " melon"]


# 공백 제거 함수
def KillEmpty(word):
    target = list(word)
    word_r = ""

    for i in target:
        if i != " ":
            word_r += i

    return word_r


fruit_list = [KillEmpty(i) for i in fruit]


fruit_dict = {key: len(key) for key in fruit_list}
print(fruit_dict)


# 연습문제 5-B
fruit = [" apple ", "banana", " melon"]

fruit_list = [i.replace(" ", "") for i in fruit]
fruit_dict = {key: len(key) for key in fruit_list}
print(fruit_dict)


# 연습문제 6
n = int(input())

n_list = [i for i in range(1, n + 1)]
result_dict = {n: n ** 2 for n in n_list}
print(result_dict)


# 연습문제 7
LETTERS, DIGITS = 0, 0

a = input()
a.replace(" ", "")

for i in a:
    try:
        int(i)
    except:
        if ("a" <= i <= "z") or ("A" <= i <= "Z"):
            LETTERS += 1
    else:
        DIGITS += 1

print("{0} {1}".format("LETTERS", LETTERS))
print("{0} {1}".format("DIGITS", DIGITS))


# 연습문제 8
UC, LC = 0, 0

a = input()

for i in list(a):
    if "a" <= i <= "z":
        LC += 1
    elif "A" <= i <= "Z":
        UC += 1

print("{0} {1}".format("UPPER CASE", UC))
print("{0} {1}".format("LOWER CASE", LC))


# 연습문제 9
beer = {"하이트": 2000, "카스": 2100, "칭따오": 2500, "하이네켄": 4000, "버드와이저": 500}
beer_up = {item[0]: item[1] * 1.05 for item in beer.items()}

# print("{0}{1}".format(beer, "            # 인상 전"))
# print("{0}{1}".format(beer_up, "  # 인상 후"))
print(beer)
print(beer_up)


# 연습문제 10
word = input()
input = sorted(list(set(word)))

result_dict = {}

# 각각의 요소들 세기
for a in input:
    cnt = 0

    for word_sep in word:
        if word_sep == a:
            cnt += 1

    result_dict[a] = cnt

# 각각의 요소 출력
for item in result_dict.items():
    print("{0},{1}".format(item[0], item[1]))
