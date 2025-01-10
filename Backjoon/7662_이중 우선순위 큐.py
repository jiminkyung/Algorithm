# 문제집 - 0x16강 - 이진 검색 트리


# 문제: https://www.acmicpc.net/problem/7662

# 도움이 됐던 질문글👉 https://www.acmicpc.net/board/view/148580
# 메모리: 181816KB / 시간: 3860ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

def solution():
    k = int(input())
    L, S = [], []  # L: 최대힙, S: 최소힙
    length = 0
    status = {}  # 숫자들의 상태(갯수)를 저장할 딕셔너리

    for _ in range(k):
        cmd, num = input().rstrip().split()
        num = int(num)

        if cmd == "I":
            heappush(L, -num)
            heappush(S, num)
            length += 1
            status[num] = status.get(num, 0) + 1
        else:
            if length <= 0:
                continue
            if num == 1:
                # 만약 숫자의 갯수가 0이라면 이미 힙에서 추출했다는 뜻이므로,
                # 아직 추출되지 않은 숫자를 찾을때까지 pop
                while True:
                    n = -heappop(L)
                    if status[n] > 0:
                        status[n] -= 1
                        break
            else:
                while True:
                    n = heappop(S)
                    if status[n] > 0:
                        status[n] -= 1
                        break
            length -= 1
    
    # 길이가 0이라면 "EMPTY" 반환
    if length <= 0:
        return "EMPTY"
    
    # 아니라면 0이 아닌 숫자 중 최대, 최소값 반환
    while True:
        _max = -heappop(L)
        if status[_max] > 0:
            break
    
    while True:
        _min = heappop(S)
        if status[_min] > 0:
            break
    
    return f"{_max} {_min}"


for _ in range(int(input())):
    print(solution())