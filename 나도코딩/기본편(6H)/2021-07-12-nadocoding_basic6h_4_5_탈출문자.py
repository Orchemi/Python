# ----------------------------------------------------------
# 탈출문자
#   문장을 두 문장으로 나누어 출력하고 싶을 때

print("백문이 불여일견 백견이 불여일타")  # 이 문장을 두 줄로 나누고 싶을 때
print("백문이 불여일견\n백견이 불여일타")  # \n을 입력한다.


# 다음의 출력값을 얻고 싶다.
#   그는 "잠 자고 싶다." 라고 말했다.  # 큰 따옴표 중복 사용 불가
print('그는 "잠 자고 싶다." 라고 말했다.')  # 아예 문자열을 작은 따옴표로 감싸기
print("그는 \"잠 자고 싶다.\" 라고 말했다.")  # 역슬러시(\)를 앞에 붙인 따옴표는 문자 그대로 문장에 삽입됨


# 다음의 출력값을 얻고 싶다.
#   print("C:\Users\Nadocoding\Desktop\Python>")
print("C:\\Users\\Nadocoding\\Desktop\\Python>")  # \\ : 문장 내에서 \ 출력


# \r : 커서를 맨 앞으로 이동.
print("Red Apple\rPine")

'''
출력값 : PineApple
1) Red Apple
2) \r 영향으로 커서가 맨 앞으로 옮겨지며 Red_ 을 블럭으로 잡아버림
3) Pine이 입력되며 Red_가 삭제, PineApple 출력
'''


# \b : backspace(한 글자 삭제)
print("Redd\bApple")  # 출력값 : RedApple


# \t : tap(tab 1회 입력)
print("Red\tApple")  # 출력값 : Red    Apple



#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
