# 연습문제 1
a = int(input())
print("{0:.2f} inch => {1:.2f} cm".format(a, a*2.54))


# 연습문제 2
a = int(input())
print("{0:.2f} kg => {1:.2f} lb".format(a, a*2.2046))


# 연습문제 3
a = int(input())
b = a * (180/100) + 32

print("{0:.2f} ℃ =>  {1:.2f} ℉".format(a, b))


# 연습문제 4
f = int(input())
c = (f - 32) * (100/180)

print("{0:.2f} ℉ =>  {1:.2f} ℃".format(f, c))


# 연습문제 5
# 문제 제시
t_a = 100

t_b = 200
s_b = 0
w_b = 200

# (용질의 무게) = (용액의 무게) * (용액의 농도)
s_a = 100 * (20 / 100)

# (용매의 무게) = (용액의 무게) - (용질의 무게)
w_a = 100 - s_a

# 전체 용액의 농도(%)
ans = ((s_a + s_b) / (t_a + t_b)) * 100

print("혼합된 소금물의 농도: {0:.2f}%".format(ans))
