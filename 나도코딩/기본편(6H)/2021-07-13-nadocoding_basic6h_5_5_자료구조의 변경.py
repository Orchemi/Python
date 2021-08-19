# ----------------------------------------------------------
# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu)  # 출력값 : {'주스', '커피', '우유'}

print(menu, type(menu))  # 출력값 : {'커피', '주스', '우유'} <class 'set'>

menu = list(menu)
print(menu, type(menu))  # 출력값 : ['커피', '우유', '주스'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu))  # 출력값 : ('우유', '커피', '주스') <class 'tuple'>

menu = set(menu)
print(menu, type(menu))  # 출력값 : {'커피', '주스', '우유'} <class 'set'>

#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
