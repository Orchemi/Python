# ----------------------------------------------------------
# 파일 입출력
#   파일을 열어서 점수 정보를 쓰는 기능

# 1. 내용 덮어쓰기

score_file = open("score.txt", "w", encoding="utf8")
# score.txt : 파일명
# w : write, 쓰기 위한 목적
# utf8 정의가 되지 않으면 한글을 쓸 때 이상한 형태로 쓰일 수 있다.

print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()  # file을 여는 경우 항상 닫아주어야 한다.

# 실행시 같은 directory 내에 score.txt가 생긴다.
# score.txt 내용은 다음과 같다.
# 수학 : 0
# 영어 : 50

# 기존 score.txt 파일에 덮어쓰기가 된다.


# 2. 내용 추가하기

score_file = open("score.txt", "a", encoding="utf8")
# score.txt : 파일명
# a : append, 내용을 추가한다.

score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
# .write()를 통했을 때에는 줄바꿈이 없으므로 \n을 넣어준다.

score_file.close()

# 실행시 score.txt 파일은 다음과 같다.
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100


# 3. 내용 불러오기
score_file = open("score.txt", "r", encoding="utf8")
# r : read, 파일에 있는 내용을 읽어오는 목적

## 가. 파일에 있는 모든 내용 불러오기
print(score_file.read())
score_file.close()

# 출력값 :
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

## 나. 파일에 있는 내용을 한 줄씩 불러오기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

# 한 줄 읽고 커서는 다음 줄로 이동

# 출력값 :
# 수학 : 0
#
# 영어 : 50
#
# 과학 : 80
#
# 코딩 : 100

# print문은 줄바꿈을 해주기 때문에 한 줄 공백 발생
# 줄바꿈 안 하고 싶다면 print(score_file.readline(), end="")


## 다. 파일의 데이터가 몇 줄인지 모를 때 불러오기
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:    # line이 없는 경우 = 읽을 내용이 없는 경우 = 문서가 끝난 경우
        break       # if 조건문 탈출
    print(line)     # line 내용 출력
score_file.close()


## 라. list에 정보를 한 줄씩 불러와 넣어 처리하기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # 모든 데이터를 읽어와서 list 형태로 저장

for line in lines:
    print(line, end="")
score_file.close()



#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s
