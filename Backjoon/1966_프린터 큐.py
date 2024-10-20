# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/1966
# 메모리: 34008KB / 시간: 64ms
from sys import stdin
from collections import deque


input = stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    doc = deque(zip(map(int, input().split()), range(N)))
    
    cnt = 1
    while True:
        m = max(doc)
        curr, idx = doc.popleft()

        if curr == m[0]:
            if idx == M:
                break
            cnt += 1
        else:
            doc.append((curr, idx))
    
    print(cnt)


# 실행시간 1위인 코드 (32ms)
# 출처👉 https://www.acmicpc.net/source/84367453
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    val = list(map(int, input().split()))  # 입력값 리스트
    arr = [(i, val[i]) for i in range(n)]  # (인덱스, 입력값) 형태로 저장한 리스트
    val.sort(reverse=True)  # 입력값들을 내림차순으로 정렬

    i = 0
    count = 0

    while True:
        if arr[i][1] == val[count]:  # i번째 값 == 현재 리스트에서 가장 큰 값 일때,
            if arr[i][0] == m:  # i가 m이라면 count 출력 후 break
                print(count + 1)
                break
            count += 1  # 아니라면 count 횟수 증가

        else:  # 가장 큰 값이 아니라면, 현재 arr[i]값을 arr에 다시 append
            arr.append((arr[i]))

        i += 1