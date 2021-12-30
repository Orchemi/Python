# 1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.

# Sol A
a = input("1~9 사이의 정수 a를 입력하십시오. : ")

a1 = 1*a
a2 = 2*a
a3 = 3*a
a4 = 4*a

sum = int(a1) + int(a2) + int(a3) + int(a4)

print(sum)

# Sol B
a = int(input("1~9 사이의 정수 a를 입력하십시오. : "))

a1 = 1*a
a2 = 11*a
a3 = 111*a
a4 = 1111*a

sum = a1 + a2 + a3 + a4
print(sum)

# Sol C
a = int(input("1~9 사이의 정수 a를 입력하십시오. : "))

sum = 1234 * a
print(sum)
