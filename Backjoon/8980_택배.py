# 문제집 - 0x11강 - 그리디


# 문제: https://www.acmicpc.net/problem/8980

# ⭐ 받는 마을 기준으로 정렬해야함. 트럭 공간을 더 빨리 비울수록 가능한 적재량이 늘어나기 때문!
# 메모리: 34456KB / 시간: 960ms
from sys import stdin


input = stdin.readline

N, C = map(int, input().split())
M = int(input())
boxes = [tuple(map(int, input().split())) for _ in range(M)]
boxes.sort(key=lambda x: x[1])  # 받는 마을 번호 기준으로 정렬

capacity = [C] * (N + 1)  # 각 마을의 트럭 최대 용량
total_box = 0

for s, e, box in boxes:
    available = min(capacity[s:e])  # s ~ e 마을 사이에서 가능한 최대 공간
    max_box = min(box, available)  # 실제로 배송 가능한 상자 수

    for i in range(s, e):
        capacity[i] -= max_box  # 가능한 상자 수만큼 s ~ e 공간 업데이트
    
    total_box += max_box

print(total_box)