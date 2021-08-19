# ----------------------------------------------------------
# 모듈(Module)
#   필요한 것들끼리 부품처럼 만들어진 파일
#   같은 파이썬 디렉토리에 있어야 사용할 수 있다.

# theater_module.py 내용
"""
# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원입니다.".format(people, people*10000))

# 조조할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원입니다.".format(people, people*6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원입니다.".format(people, people*4000))
"""


# module의 활용
import theater_module
theater_module.price(3)  # 3명이 영화를 보는 가격
theater_module.price_morning(4)  # 4명이 조조할인영화를 보는 가격
theater_module.price_soldier(5)  # 5명이 군인할인영화를 보는 가격


# module 호출의 간소화
#   theater_module을 mv라는 별명으로 호출

import theater_module as mv

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)


# module의 완전호출
from theater_module import *
price(3)
price_morning(4)
price_soldier(5)


# module의 선택호출
#   군인할인가격 없이 일반과 조조할인 가격만 호출하겠다.
from theater_module import price, price_morning
price(3)
price_morning(4)
price_soldier(6)

# 출력결과는 다음 결과처럼 price_soldier에 대해 오류가 발생한다.
"""
    price_soldier(6)
NameError: name 'price_soldier' is not defined
3명 가격은 30000원입니다.
4명 조조 할인 가격은 24000원입니다.
"""


# module의 선택호출 후 별명 부여
#   price_soldier를 price라는 별명으로 호출하겠다.
from theater_module import price_soldier as price
price(3)




#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
