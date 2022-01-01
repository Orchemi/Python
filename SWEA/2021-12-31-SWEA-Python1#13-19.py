# 연습문제 1
A = int(input())

for B in range(1, A + 1):
    if (A % B) == 0:
        print("{0}(은)는 {1}의 약수입니다.".format(B, A))


# 연습문제 2
num_ys = 0
A = int(input())

for B in range(1, A + 1):
    if (A % B) == 0:
        num_ys += 1
        print("{0}(은)는 {1}의 약수입니다.".format(B, A))

if num_ys == 2:
    print("{0}(은)는 1과 {0}로만 나눌 수 있는 소수입니다.".format(A))


# 연습문제 3
alpha = input()
alpha_num = ord(alpha)

if 65 <= alpha_num <= 90:
    print("{0} 는 대문자 입니다.".format(alpha))
elif 97 <= alpha_num <= 122:
    print("{0} 는 소문자 입니다.".format(alpha))


# 연습문제 4
lst = ["가위", "바위", "보"]
Man1 = input()
Man2 = input()

if not ((Man1 in lst) and (Man2 in lst)):
    Result = "입력 오류"
elif Man1 == Man2:
    Result = "Draw"
elif Man1 == lst[0]:

    if Man2 == lst[1]:
        Result = "Man2 Win!"
    elif Man2 == lst[2]:
        Result = "Man1 Win!"
elif Man1 == lst[1]:

    if Man2 == lst[0]:
        Result = "Man1 Win!"
    elif Man2 == lst[2]:
        Result = "Man2 Win!"
elif Man2 == lst[2]:

    if Man2 == lst[0]:
        Result = "Man1 Win!"
    elif Man2 == lst[1]:
        Result = "Man2 Win!"

print("Result : " + Result)


# 연습문제 5-A
alpha = input()

if len(alpha) == 1:
    alpha_num = ord(alpha)
else:
    alpha_num = 0

# 소문자 -> 대문자
if 97 <= alpha_num <= 122:
    print("%c(ASCII: %d) = > %c(ASCII: %d)" %
          (alpha, alpha_num, alpha_num - 32, alpha_num - 32))
# 대문자 -> 소문자
elif 65 <= alpha_num <= 90:
    print("%c(ASCII: %d) = > %c(ASCII: %d)" %
          (alpha, alpha_num, alpha_num + 32, alpha_num + 32))
# 기타
else:
    print(alpha)


# 연습문제 5-B
alpha = input()

if len(alpha) > 1:
    print(alpha)
elif alpha.islower():
    print("%s(ASCII: %d) = > %s(ASCII: %d)" %
          (alpha, ord(alpha), alpha.upper(), ord(alpha.upper())))
elif alpha.isupper():
    print("%s(ASCII: %d) = > %s(ASCII: %d)" %
          (alpha, ord(alpha), alpha.lower(), ord(alpha.lower())))
else:
    print(alpha)


# 연습문제 5-C
alpha = input()

if 'a' <= alpha <= 'z':     # alpha가 소문자일 경우
    print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(
        alpha, ord(alpha), alpha.upper(), ord(alpha.upper())))
elif 'A' <= alpha <= 'Z':  # alpha가 대문자일 경우
    print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(
        alpha, ord(alpha), alpha.lower(), ord(alpha.lower())))
else:   # alpha가 소문자/대문자 가 아닌 경우
    print(alpha)


# 연습문제 7
result = ""

for i in range(1, 200):
    if ((i % 7 == 0) and (i % 5 != 0)):
        result += "%d," % i

print(result[0:len(result)-1])


# 연습문제 8
result = ""

for i in range(100, 300):
    i_s = str(i)
    if((int(i_s[0]) % 2 == 0) and (int(i_s[1]) % 2 == 0) and (int(i_s[2]) % 2 == 0)):
        # result += "%d," % i
        result += "%d," % i

print(result[0:len(result)-1])
