# ----------------------------------------------------------
# 외장함수
#   직접 import 해서 사용해야 하는 함수

## 가. 함수 출처
"""
google 검색
'list of python modules'

Python Module Index 라는 사이트에서 외장함수 목록 조회 가능
"""

## 나. glob
#   경로 내의 폴더 / 파일 조회 (windows의 dir 명령어와 같다.)
import glob
print(glob.glob("*.py"))  # 현재 디렉토리 내에 확장자가 py 인 모든 파일 조회


## 다. os
#   운영체제에서 제공하는 기본 기능 (ex. 폴더 생성/제거 등)

### 1) getcwd
import os
print(os.getcwd())  # 현재 디렉토리 표시
# 출력값 : C:\Intellij\python\나도코딩\기본편(6H)

### 2) makedirs, rmdir
folder = "sample_dir"

if os.path.exists(folder):  # folder(sample_dir) 라는 폴더가 있으면 if문 실행
    print("이미 존재하는 폴더입니다.")
    os. rmdir(folder)  # folder 폴더를 삭제
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)  # folder 폴더 생성
    print(folder, "폴더를 생성하였습니다.")

# 출력값 :
# 1회 실행 : sample_dir 폴더를 생성하였습니다. sample_dir 폴더 생성
# 2회 실행 : 이미 존재하는 폴더입니다. 폴더를 삭제하였습니다. sample_dir 폴더 삭제


### 3) listdir
#   현재 디렉토리 내의 파일을 모두 출력
#   glob과 비슷하지만 선택적이지 않고 모두 출력하는 것이 차이점
print(os.listdir())


## 라. time
import time
print(time.localtime())
# 출력값 : time.struct_time(tm_year=2021, tm_mon=7, tm_mday=20, tm_hour=13, tm_min=35, tm_sec=31, tm_wday=1, tm_yday=201, tm_isdst=0)

print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 출력값 : 2021-07-20 13:36:33


## 마. datetime
import datetime
print("오늘 날짜는", datetime.date.today())
# 출력값 : 오늘 날짜는 2021-07-20

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()  # 오늘 날짜 저장
td = datetime.timedelta(days=100)  # +100일 저장
print("우리가 만난지 100일은", today + td)  # 우리가 만난지 100일 후
# 출력값 : 우리가 만난지 100일은 2021-10-28


#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s

