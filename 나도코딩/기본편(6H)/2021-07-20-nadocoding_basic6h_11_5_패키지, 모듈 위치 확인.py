# ----------------------------------------------------------
# 패키지, 모듈 위치 확인 'inspect'
#   지금까지는 같은 디렉토리나 같은 파이썬 라이브러리에 있는 모듈을 참조하였는데,
#   이 모듈이나 패키지의 위치를 확인할 수 있는 방법을 알아보자.
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
# 출력결과 : C:\Users\(내 이름)\AppData\Local\Programs\Python\Python39\lib\random.py

print(inspect.getfile(thailand))
# 출력결과 : C:\Intellij\python\나도코딩\기본편(6H)\travel\thailand.py




#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
