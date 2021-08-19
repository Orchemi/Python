# ----------------------------------------------------------
# Quiz 11

## 문제
"""
Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

조건 : 모듈 파일명은 byme.py 로 작성

(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com
"""

## 나의 작성 코드
'''
같은 디렉토리 내에 byme.py 모듈 생성 후 아래 코드를 입력

def sign():
    print("""이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com
""")
'''

import byme

byme.sign()



## 모범 답안

'''
같은 디렉토리 내에 byme.py 모듈 생성 후 아래 코드를 입력

def sign():
    print("""이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com
""")
'''

import byme
byme.sign()

#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
