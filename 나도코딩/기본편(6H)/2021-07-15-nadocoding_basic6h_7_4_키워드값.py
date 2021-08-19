# ----------------------------------------------------------
# 키워드값
#   함수에서 전달받는 매개변수의 값을 순서와 관계 없이 키워드를 이용해 호출

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=20, name="김태호")

# 출력값 :
# 유재석 20 파이썬
# 김태호 20 자바




#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
