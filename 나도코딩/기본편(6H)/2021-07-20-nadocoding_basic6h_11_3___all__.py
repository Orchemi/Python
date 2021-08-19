# ----------------------------------------------------------
# __all__
# from random import *
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# 출력결과는 다음과 같다.
"""
    trip_to = vietnam.VietnamPackage()
NameError: name 'vietnam' is not defined
"""

# 오류는 왜 발생할까.
"""
* 을 쓰는 것은 travel package의 모든 것을 가져오겠다는 뜻이다.
실제로는 개발자가 이 문법상에서 공개범위를 설정해주어야 한다.
__init__ 파일에 다음과 같이 작성한다. 
"""

"""
__all__ = ["vietnam"]
"""


## __init__ 파일 수정 이후
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 출력결과는 다음과 같다.

"""
trip_to = thailand.ThailandPackage()
NameError: name 'thailand' is not defined
"""

# __init__ 파일에서 vietnam에 대해서만 공개했기 때문에
# thailand에 대해서는 공개되지 않아 오류가 발생
# __init__ 파일을 다음과 같이 수정한다.
"""
__all__ = ["vietnam", "thailand"]
"""

# 이후 ThailandPackage class의 detail() 함수 실행시 정상적으로 출력됨을 확인할 수 있다.


#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
