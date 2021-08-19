# ----------------------------------------------------------
# pip install
#   이미 잘 만들어진 package를 필요한 곳에 가져다 쓰는 것이 필요


## 1. pypi(python package index)
#   'beautifulsoup' package를 install해서 사용해보자.
#   웹페이지의 스크래핑을 쉽게 해주는 라이브러리
"""
1. google에 'pypi'를 치고 https://pypi.org/ 로 들어간다.
2. 검색창에서 'beautifulsoup'를 검색한다. (https://pypi.org/project/beautifulsoup4/)
3. pip install beautifulsoup4 copy
4. terminal에 paste
"""


## 코드의 사용
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


## pip 명령어
#   terminal에서 사용할 수 있는 pip 명령어
"""
# 현재 설치되어있는 pip 리스트 확인
pip list  

# beautifulsoup4 package의 세부정보를 확인하기
pip show beautifulsoup4  

# package의 버전을 업그레이드하기
pip install --upgrade beautifulsoup4

# package 제거
pip uninstall beautifulsoup4
"""



#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
