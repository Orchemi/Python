# ----------------------------------------------------------
# 사전(dictionary)
# - 단어, 단어에 대한 정의
# - key, key에 해당하는 value
# - key에 대한 중복이 허용되지 않음
# - 중괄호 {key:value} 로 표현

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])  # 3번 key는 '유재석'이 가지므로 출력값 : 유재석
print(cabinet[100])  # 출력값 : 김태호

print(cabinet.get(3))  # .get() : 자료형에서 해당 key의 값(value)을 가져오는 함수

# key가 할당되지 않는 경우 [] vs .get()
print(cabinet[5])  # key가 없기 때문에 KeyError 발생, 이후 프로그램 종료
print("HI")  # 프로그램이 종료되어 출력되지 않음

print(cabinet.get(5))  # key가 없기 때문에 None 발생, 이후 프로그램 진행
print("HI")  # 프로그램이 계속 진행되어 HI 출력

# .get() 이후 없는 key에서 None 발생 대신 다른 문구를 쓰고 싶을 때
print(cabinet.get(5, "사용 가능"))


# 사전 자료형에서 자료 있는지 확인
# - key in variable

print(3 in cabinet)  # True
print(5 in cabinet)  # False


# key는 문자열도 가능
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])


# 새 손님
# - C-20 key에 값이 있든 없든 '조세호' 라는 value 등록

cabinet = {"A-3":"유재석", "B-100":"김태호"}

cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)  # 출력값 : {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}


# 간 손님
# - del 함수를 이용하여 key에 해당하는 value 삭제
del cabinet["A-3"]
print(cabinet)  # 출력값 : {'B-100': '김태호', 'C-20': '조세호'}


# key들만 출력
print(cabinet.keys())  # 출력값 : dict_keys(['B-100', 'C-20'])


# value들만 출력
print(cabinet.values())  # 출력값 : dict_values(['김태호', '조세호'])


# key, value 쌍으로 출력
print(cabinet.items())  # 출력값 : dict_items([('B-100', '김태호'), ('C-20', '조세호')])


# 목욕탕 폐점
cabinet.clear()
print(cabinet)  # 출력값 : {}



#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
