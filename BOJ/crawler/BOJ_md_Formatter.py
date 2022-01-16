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


# 3.5. solved.ac에서 문제번호로 문제레벨 검색
# 3.5.1. requests pip 사용

url2 = f"https://solved.ac/search?query={input_problem_num}"
response2 = requests.get(url2).text
data2 = BeautifulSoup(response2, 'html.parser')

# 3.5.2. 문제 레벨 img 추출
img_info = data2.select('img')[0]

# 3.5.3. 문제 레벨 img 에서 alt 추출
problem_level = img_info['alt']

# 3.5.4. 문제 클래스와 티어 구분
problem_level_list = problem_level.split(' ')

# Bronze, Silver, Gold 등
problem_level_class = problem_level_list[0]
# I, II, III 등
problem_level_tier = problem_level_list[1]


# 3.5.5. 문제 클래스와 티어 dictionary 지정
problem_level_class_dict = {
    'Bronze': '🟤',
    'Silver': '⚪',
    'Gold': '🟡',
    'Platinum': '🔘',
    'Diamond': '💎',
    'Ruby': '🚨'
}

problem_level_tier_dict = {
    'I': 1,
    'II': 2,
    'III': 3,
    'IV': 4,
    'V': 5
}


# 3.5.6. dict에 대해 value 추출해서 변수에 지정
problem_class = problem_level_class_dict[problem_level_class]
problem_tier = problem_level_tier_dict[problem_level_tier]

# 3.6. 입력
txt = f"""---
title: "[BOJ][#{problem_num}][{problem_class}{problem_tier}]{problem_title}"
excerpt: "BAEKJOON Online Judge 문제 풀이"

categories:
  - BOJ

tags:
  - [BOJ, ProblemSolving, Python, {problem_level_class}]
"""

# 3.7. result에 붙이기
result = f"{txt}"

#####################################################
# 4. 입력 시간/수정 시간
# 4.1. datetime pip 이용
now = str(datetime.now())


# 4.2. 데이터 슬라이싱
date_now = f"{now[:10]}T{now[11:16]}"


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

if problem_input == "":
    problem_input == "없음"


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

if problem_output == "":
    problem_output == "없음"

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
if len(problem_limit) == 1:
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

for cnt in range(0, 20):
    try:
        sampledata = data.select('.sampledata')[cnt].text

    except:
        break

    else:
        sampledata_list.append(sampledata)


# 10.2. 예제 분리
# input 데이터 리스트 저장
sampledata_list_input = [
    item for item in sampledata_list if sampledata_list.index(item) % 2 == 0]

# output 데이터 리스트 저장
sampledata_list_output = [
    item for item in sampledata_list if sampledata_list.index(item) % 2 == 1]


# 10.3. 예제 이어붙이기
sampletxt = ""

for i in range(0, len(sampledata_list_input)):
    if sampledata_list_input[i] == "":
        sampledata_list_input[i] = "없음"

    inout_ex = f"""
입력

```python
{sampledata_list_input[i]}
```

<br>

출력

```python
{sampledata_list_output[i]}
```

<br>

"""

    if len(sampledata_list_input) == 1:
        a = f"""
{inout_ex}
"""

    else:
        a = f"""
### 예제 {i + 1}

{inout_ex}
"""

    sampletxt = f"{sampletxt}{a}"


# 10.4. txt에 입력
txt = f"""
## 예제
{sampletxt}
"""

# 10.5. result에 붙이기
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
