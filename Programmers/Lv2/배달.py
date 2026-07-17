# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12978

# 다익스트라 문제
from heapq import heappush, heappop


def solution(N, road: list[list], K):
    INF = int(1e9)
    graph = [[] for _ in range(N)]
    
    for u, v, w in road:
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    
    heap = []
    heappush(heap, (0, 0))  # 시간, 노드
    dp = [INF] * N
    dp[0] = 0
    
    while heap:
        time, node = heappop(heap)
        
        if dp[node] < time:
            continue
        
        for v, w in graph[node]:
            new_time = time + w
            
            if new_time < dp[v]:
                dp[v] = new_time
                heappush(heap, (new_time, v))
                
    return sum(dp[i] <= K for i in range(N))