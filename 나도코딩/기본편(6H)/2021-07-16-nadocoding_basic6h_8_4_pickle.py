# ----------------------------------------------------------
# pickle
#   프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장하는 것


# 1. pickle 파일 생성

import pickle   # pickle 이라는 모듈 import
profile_file = open("profile.pickle", "wb")
# w : write, 쓰기 위한 목적
# b : binary, pickle을 쓰기 위해선 반드시 정의
# pickle에서는 따로 encoding하지 않는다.

profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)

pickle.dump(profile, profile_file)
# profile에 있는 정보를 file에 저장
profile_file.close()


# 2. pickle 파일 사용
profile_file = open("profile.pickle", "rb")

# file에 있는 정보를 profile에 불러오기
profile = pickle.load(profile_file)

print(profile)  # 출력값 : {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
profile_file.close()



#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
