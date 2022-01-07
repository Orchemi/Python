# 연습문제 1
input_str = input()
print(input_str)

input_str_r = ""
for i in input_str:
    input_str_r = i + input_str_r

if input_str == input_str_r:
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")


# 연습문제 2-A
input_str = input()
input_list = input_str.split(" ")

input_str_r = ""

for i in input_list:
    input_str_r = "{0} {1}".format(i, input_str_r)

print(input_str_r)


# 연습문제 2-B
input_str = input()
input_list = input_str.split(" ")

input_list_r = reversed(input_list)
input_str_r = ""

for i in input_list_r:
    input_str_r += i + " "

print(input_str_r[:-1])


# 연습문제 3
# 입력값 저장
input_str = input()

# protocol 분리
input_list_1 = input_str.split("://")
protocol = input_list_1[0]

# host 분리
input_list_2 = input_list_1[1].split("/")
host = input_list_2[0]

# others 리스트에서 host 항목 제거
input_list_2.remove(host)

# others 리스트 문자열 합치기
others = ""
for i in input_list_2:
    others += i + "/"

# 맨 마지막 "/"" 제거
others = others[:-1]

# 출력
print("protocol: {0}".format(protocol))
print("host: {0}".format(host))
print("others: {0}".format(others))


# 연습문제 4
input_list = []

input_complete = 0

while True:
    a = input()

    if a == "":
        break
    else:
        input_list.append(a)

for i in input_list:
    print(">> {0}".format(i.upper()))


# 연습문제 5
input_str = input()
input_list = sorted(list(set(input_str.split(" "))))

result_str = ""
for i in input_list:
    result_str += i + ","

print(result_str[:-1])


# 연습문제 7
input_str = input()

for i in range(0, len(input_str), 2):
    print(input_str[i], end="")
