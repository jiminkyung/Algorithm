# 문제집 - 0x16강 - 이진 검색 트리


# 문제: https://www.acmicpc.net/problem/21939

# 반례 모음집👉 https://www.acmicpc.net/board/view/123070
# 메모리: 65952KB / 시간: 244ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline

N = int(input())
L, S = [], []
status = {}

for _ in range(N):
    P, level = map(int, input().split())
    status[P] = level
    heappush(L, (-level, -P))
    heappush(S, (level, P))

M = int(input())
for _ in range(M):
    cmd, *x = input().rstrip().split()

    if cmd == "add":
        P, level = map(int, x)
        status[P] = level
        heappush(L, (-level, -P))
        heappush(S, (level, P))
    elif cmd == "recommend":
        # heap에서 빼낸 (값, 문제)와 status[문제]를 비교한다.
        # status[문제]의 값과 heap의 값이 일치하지 않는다면 이미 풀었던 문제이므로 풀지 않은 문제를 찾을때까지 pop
        if x[0] == "1":
            level, P = heappop(L)
            while status.get(-P, 0) != -level:
                level, P = heappop(L)
            heappush(L, (level, P))  # 뺐던 문제들은 다시 넣어줌
            print(-P)
        else:
            level, P = heappop(S)
            while status.get(P, 0) != level:
                level, P = heappop(S)
            heappush(S, (level, P))
            print(P)
    else:  # solved P 일때
        del status[int(x[0])]