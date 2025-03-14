# 문제집 - 0x1D강 - 다익스트라 알고리즘


# 문제: https://www.acmicpc.net/problem/22870

# 5719_거의 최단 경로 문제와 비슷한 매커니즘이다. 하지만 첫번째 다익스트라 후 최단경로를 처리하는 방식이 다름.
# 도움이 됐던 반례👉 https://www.acmicpc.net/board/view/78074

# 메모리: 192836KB / 시간: 3672ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline
INF = float("inf")

def main():
    # 1. 첫번째 다익스트라를 실행하며 이전 노드들(prev) 저장
    def first_dijkstra() -> tuple[list, int]:
        dist = [INF] * (N+1)
        prev = [[] for _ in range(N+1)]
        dist[S] = 0

        heap = [(0, S)]

        while heap:
            d, curr = heappop(heap)

            if dist[curr] < d:
                continue

            for nxt, nxt_d in graph[curr]:
                new_d = d + nxt_d
                if new_d < dist[nxt]:
                    prev[nxt] = [curr]
                    dist[nxt] = new_d
                    heappush(heap, (new_d, nxt))
                elif new_d == dist[nxt]:
                    prev[nxt].append(curr)
        return prev, dist[E]
    
    # 2. prev 노드를 토대로 최단경로에 사용된 노드들을 방문처리
    # 🚨 graph를 갱신하는 방식 -> 시간초과!
    def remove(prev: list) -> list:
        visited = [False] * (N+1)
        candidates = [[] for _ in range(N+1)]
        stack = [E]

        while stack:
            curr = stack.pop()

            if visited[curr]:
                continue

            visited[curr] = True
            for prev_node in prev[curr]:
                heappush(candidates[prev_node], curr)  # S -> E 방향으로 저장해줌
                stack.append(prev_node)
        
        visited = [False] * (N+1)
        curr = S
        while True:
            # candidates[curr]: S -> E 최적경로들 중 curr 다음으로 갈 수 있는 경로들
            nxt = heappop(candidates[curr])
            if nxt == E:  # S, E는 방문처리가 되면 안되므로 바로 break
                break
            visited[nxt] = True  # 해당 경로는 방문처리해줌

            curr = nxt
        
        return visited
    
    # 3. 끝점부터 시작점까지 다시 한 번 다익스트라. 방문처리된 노드(최단 경로)는 제외시킴.
    def second_dijkstra(visited: list) -> int:
        dist = [INF] * (N+1)
        dist[E] = 0
        heap = [(0, E)]

        while heap:
            d, curr = heappop(heap)

            if dist[curr] < d:
                continue

            for nxt, nxt_d in graph[curr]:
                if visited[nxt]:  # 방문처리된 경로 = 최적경로로 선택된 경로들
                    continue
                new_d = d + nxt_d
                if new_d < dist[nxt]:
                    dist[nxt] = new_d
                    heappush(heap, (new_d, nxt))
        return dist[S]


    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))

    S, E = map(int, input().split())
    prev, go = first_dijkstra()
    visited = remove(prev)
    back = second_dijkstra(visited)
    
    print(go + back)


main()