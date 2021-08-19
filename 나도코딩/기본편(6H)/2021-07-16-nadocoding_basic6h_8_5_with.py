# ----------------------------------------------------------
# with

# 1. pickle을 이용하는 방법
#   file의 정보를 읽어와서 변수에 저장하는 방법
#   with open("file", "rb") as variable:

import pickle
with open("profile.pickle", "rb") as profile_file:
    # profile.pickle에서 데이터를 읽어와서 profile_file 변수에 값 저장

    print(pickle.load(profile_file))
    # 출력값 : {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}

# with 문을 탈출하면서 profile.pickle file을 종료하므로 따로 .close() 문을 쓸 필요 없다.


# 2. pickle이 아닌 일반 파일을 이용하는 방법
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

# 실행결과
# study.txt 파일이 같은 디렉토리 내에 생기고, '파이썬을 열심히 공부하고 있어요.' 라는 문장이 있다.

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

# 출력값 : 파이썬을 열심히 공부하고 있어요.

#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
