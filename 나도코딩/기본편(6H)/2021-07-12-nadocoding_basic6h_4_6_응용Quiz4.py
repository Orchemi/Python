# ----------------------------------------------------------
'''
사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

ex) http://naver.com
규칙 1 : http:// 부분은 제외 => naver.com
규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙 3 : 남은 글자 중 처음 세 자리 + 글자 개수 + 글자 내 'e' 개수 + "!" 로 구성
    => 생성된 비밀번호 : nav51!
'''

page = "http://naver.com"

page1 = page.replace("http://", "")
dot_index = page1.find(".")
page2 = page1[:dot_index]
password = page2[:3] + str(len(page2)) + str(page2.count("e")) + "!"

print("생성된 비밀번호 : " + password)




''' 답안
url = "http://naver.com"
my_str = url.replace("http://", "")  # 규칙 1
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

'''


#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
