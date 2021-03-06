# ----------------------------------------------------------
# 연산자
print(2**3)  # 2^3=8
print(5%3)   # 5/3의 나머지=2
print(5//3)  # 5/3의 몫=1


# 논리 1
print(10 > 3)  # True
print(3 == 3)  # 앞 값과 뒷 값이 같은지의 boolean 형 : True
print(3 + 4 == 7)  # True


# 논리 2
print(1 != 3)  # '!=' : 같지 않다. 1과 3은 같지 않기 때문에 True
print(not(1 != 3))  # 1과 3은 같지 않으므로 True 인데 not으로 씌웠으므로 False


# 연결
print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))  # True
print((3 > 0) or (3 > 5))  # True or False : True
print((3 > 0) | (3 > 5))  # True or False : True


# 연속
print(5 > 4 > 3)  # True & True : True
print(5 > 3 > 4)  # True & False : False


#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
