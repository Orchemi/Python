# 1. pip import
from datetime import *
from html.parser import HTMLParser
import clipboard
import requests
from bs4 import BeautifulSoup

#####################################################
# 2. 변수 초기화

result = ""
txt = ""

#####################################################
# 3. title
# 3.1. 문제 번호 입력
input_problem_num = input("문제 번호 입력 : ")
url = f"https://www.acmicpc.net/problem/{input_problem_num}"


# 3.2. requests pip 사용
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')


# 3.3. 제목 추출
problem_title = data.select_one('#problem_title').text


# 3.4. 문제 번호 폼
if int(input_problem_num) < 10000:
    problem_num = "0" + input_problem_num
else:
    problem_num = input_problem_num


# 3.5. 입력
txt = f"""---
title: "[BOJ][#{problem_num}][🟤⚪🟡🔘💎🚨0]{problem_title}"
excerpt: "BAEKJOON Online Judge 문제 풀이"

categories:
  - BOJ

tags:
  - [BOJ, ProblemSolving, Python, Bronze]
"""

# 3.6. result에 붙이기
result = f"{txt}"

#####################################################
# 4. 입력 시간/수정 시간
# 4.1. datetime pip 이용
now = str(datetime.now())


# 4.2. 데이터 슬라이싱
date_now = now[:10] + "T" + now[11:16]


# 4.3. 입력
txt = f"""
date: {date_now}
last_modified_at: {date_now}

author_profile: true

toc: true

toc_label: "목차"
toc_icon: "bars"
toc_sticky: true
---
"""

# 4.4. result에 붙이기
result = f"{result}\n{txt}"

#####################################################
# 5. 문제 출처

txt = f"""
## 문제 출처

[BAEKJOON Online Judge #{input_problem_num}]({url})

<br>
"""

result = f"{result}\n{txt}"

#####################################################
# 6. 문제
# 6.1. 문제 추출
problem_description = data.select_one('#problem_description').text


# 6.2. 입력
txt = f"""
## 문제

{problem_description}

<br>
"""


# 6.3. result에 붙이기
result = f"{result}\n{txt}"

#####################################################
# 7. 입력
# 7.1. 입력 추출
problem_input = data.select_one('#problem_input').text


# 7.2. 입력
txt = f"""
## 입력

{problem_input}

<br>
"""


# 7.3. result에 붙이기
result = f"{result}\n{txt}"

#####################################################
# 8. 출력
# 8.1. 출력 추출
problem_output = data.select_one('#problem_output').text


# 8.2. 입력
txt = f"""
## 출력

{problem_output}

<br>
"""


# 8.3. result에 붙이기
result = f"{result}\n{txt}"

#####################################################
# 9. 제한
# 9.1. 제한 추출
problem_limit = data.select_one('#problem_limit').text

# 9.2. 입력
if problem_limit == " ":
    txt = ""
else:
    txt = f"""

## 제한

{problem_limit}

<br>
"""


# 9.3. result에 붙이기
result = f"{result}{txt}"

#####################################################
# 10. 예제
# 10.1. 예제 추출
sampledata_list = []
cnt = 0

for cnt in range(0, 21):
    try:
        sampledata = data.select('.sampledata')[cnt].text

    except:
        break

    else:
        sampledata_list.append(sampledata)


# 10.2. 예제 분리
sampledata_list_input = [
    item for item in sampledata_list if sampledata_list.index(item) % 2 == 0]
sampledata_list_output = [
    item for item in sampledata_list if sampledata_list.index(item) % 2 == 1]


# 10.3. 예제 이어붙이기
sampletxt = ""

for i in range(0, len(sampledata_list_input)):
    if sampledata_list_input[i] == "":
        sampledata_list_input[i] = "없음"

    a = f"""
### 예제 {i + 1}

입력

```python
{sampledata_list_input[i]}
```

출력

```python
{sampledata_list_output[i]}
```

<br>

"""

    sampletxt = f"{sampletxt}{a}"


# 10.4. txt에 입력
txt = f"""
## 예제
{sampletxt}
"""

# 10.4. result에 붙이기
result = f"{result}\n{txt}"

#####################################################
# 11. etc
# 11.1. 나머지 문자 입력
txt = """
## My Sol

```python
# empty
```

<br>

## 결과

> 맞았습니다!!

<br>

## 모범답안

```python
# empty
```
"""

# 11.2. result에 붙이기
result = f"{result}\n{txt}"

#####################################################
# 12. result를 클립보드에 copy
clipboard.copy(result)
print("복사가 완료되었습니다!")
