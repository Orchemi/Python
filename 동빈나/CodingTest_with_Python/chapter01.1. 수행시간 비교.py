from random import *
import time

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100))  # 1부터 100 사이의 랜덤한 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # 스와프
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()  # 측정 종료

# 수행시간 출력
print("선택 정렬 성능 측정: ", round(end_time - start_time,20))


# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time()  # 측정 종료

# 수행시간 출력
print("선택 정렬 성능 측정: ", round(end_time - start_time,20))