# 플로이드 워셜


# 문제: https://www.acmicpc.net/problem/1058
# 메모리: 32412KB / 시간: 48ms
from sys import stdin


input = stdin.readline
INF = float("inf")

def main():
    # A와 B가 2-친구이려면 A-B or A-C-B 가 성립해야함.
    N = int(input())
    graph = [[INF] * N for _ in range(N)]

    # 1. 친구 그래프 생성. A-B가 친구라면 1로 저장.
    for i in range(N):
        line = input().rstrip()
        for j in range(i+1, N):
            if line[j] == "Y":
                graph[i][j] = 1
                graph[j][i] = 1
    
    # 2. 플로이드 워셜 수행
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    max_cnt = 0

    # 3. 한명씩 순회하며 2-친구가 몇명인지 체크.
    # 2-친구가 성립하려면 친구 사이 거리가 1~2이어야 함.
    for A in range(N):
        cnt = 0
        for B in range(N):
            # 자기 자신은 친구가 아님. 플로이드워셜 후에 A-A값이 갱신되므로 체크해줘야함.
            if A != B and graph[A][B] <= 2:
                cnt += 1
        max_cnt = max(cnt, max_cnt)
    
    print(max_cnt)


main()