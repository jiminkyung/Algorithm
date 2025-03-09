# 문제집 - 0x1D강 - 다익스트라 알고리즘


# 문제: https://www.acmicpc.net/problem/13907

# 로직은 크게 다르지 않지만 최적화 유/무에 따라 통과/시간초과로 나뉜다... 최적화의 중요성을 느끼게해준 문제.
# 다시 풀어볼만한 문제다.
# 참고👉 https://velog.io/@vkdldjvkdnj/boj13907
"""
⭐ 시간초과 요인
1. heap에 삽입 시 (총 비용, 현재위치, 사용한 간선 수) 순서로 저장.
=> (총 비용, 사용한 간선 수, 현재위치) 로 변경. 비용이 같다면 간선 수가 더 작은값이 우선시되게끔 수정

2. heap에서 꺼낸 뒤 dp[curr][edges] < cost로 현재 사용한 간선 수와 정확히 일치하는 경우와만 비교.
=> 0부터 edges까지 비교. 만약 지금보다 간선을 더 적게 사용한 경우의 비용이 cost보다 작다면 현재 값은 필요없으므로 flag=False 처리.

3. 세금 인상 과정에서 체크할 간선 수 범위를 매번 0부터 N까지로 설정.
=> 현재까지의 최소비용보다 간선을 더 많이 사용한 경우는 탐색할 필요 X. 이전 최대비용의 간선 수 까지만 체크. => range(t+1)

4. 다익스트라만 함수로 떼어놓음. 전체 함수화 X
=> main()으로 묶어놓으니 더 빠르다. 전역변수 참조를 최소화해서 그런듯.
"""
# 메모리: 49256KB / 시간: 188ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline
INF = float("inf")


def main():
    N, M, K = map(int, input().split())
    S, D = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    # 양방향 도로임
    for _ in range(M):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    taxes = [int(input()) for _ in range(K)]  # 인상될 세금 리스트


    def dijkstra() -> list:
        dp = [[INF] * N for _ in range(N + 1)]
        dp[S][0] = 0
        heap = [(0, 0, S)]  # 비용, 사용한 간선 수, 현재 노드

        while heap:
            curr_cost, edges, curr = heappop(heap)

            # 🗝️ 간선을 더 적게 사용한 경우가 효율적일경우
            # flag = True로 설정 후 break
            flag = False
            for i in range(edges + 1):
                if dp[curr][i] < curr_cost:
                    flag = True
                    break

            # 사용한 간선 수가 N-1개 이상(전체를 방문한 경우)이거나 flag=True라면 pass!
            if edges >= N - 1 or flag:
                continue

            for nxt, nxt_cost in graph[curr]:
                new_edges = edges + 1
                if new_edges >= N:
                    continue

                new_cost = curr_cost + nxt_cost
                if new_cost < dp[nxt][new_edges]:
                    dp[nxt][new_edges] = new_cost
                    heappush(heap, (new_cost, new_edges, nxt))
        return dp


    dp = dijkstra()

    min_cost = INF  # 최소비용
    t = 0  # 최소비용에서 사용한 간선 수

    for edges in range(N):
        if dp[D][edges] < min_cost:
            min_cost = dp[D][edges]
            t = edges

    print(min_cost)

    total_tax = 0
    for tax in taxes:
        total_tax += tax
        min_cost = INF
        for edges in range(t + 1):  # 🗝️ 이전 최소비용이 사용한 간선 수까지만 탐색함.
            if dp[D][edges] != INF:
                cost = dp[D][edges] + edges * total_tax
                if cost < min_cost:
                    min_cost = cost
                    t = edges

        print(min_cost)


main()  # 함수화 한것과 안한것의 차이가 꽤 크다. 하기 전 - 메모리: 50132KB, 시간: 228ms