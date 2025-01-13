# 문제집 - 0x16강 - 이진 검색 트리


# 문제: https://www.acmicpc.net/problem/23326

# 일단 이 문제는 Python3로 통과된 사람이 아직 없다.
# PyPy3로 제출해도 시간초과... 아직 해결 방법을 찾기 못함.
# 아래 코드는 66%까지 갔던 코드.

from sys import stdin
from bisect import bisect_left, insort_left


input = stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
landmark = [i for i in range(N) if A[i]]  # 명소만 따로 저장

curr = 0
query = iter(map(int, stdin.read().split()))

for q in query:
    # 1: 명소 toggle
    if q == 1:
        area = next(query) - 1
        idx = bisect_left(landmark, area)

        if idx < len(landmark) and landmark[idx] == area:  # 이미 명소인 경우 해제
            landmark.pop(idx)
        else:  # 명소가 아닌 경우 오름차순에 맞게 삽입
            insort_left(landmark, area)

    # 2: 이동
    elif q == 2:
        curr = (curr + next(query)) % N
    
    # 3: 가까운 명소까지의 거리
    else:
        if not landmark:
            print(-1)
            continue
        
        # 현재 위치보다 크거나 같은 첫 명소의 위치
        idx = bisect_left(landmark, curr)

        if idx == len(landmark):  # 현재 위치보다 큰 명소가 없으면 가장 첫번째 명소로
            print(N - curr + landmark[0])
        else:
            print(landmark[idx] - curr)