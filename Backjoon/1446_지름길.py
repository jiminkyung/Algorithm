# 최단 경로
# 다익스트라
# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/1446

# 다익스트라 or DP를 사용해서 풀 수 있음. N의 크기가 작아 DP로 풀어도 빠르게 통과 가능.

# 1) 다익스트라 사용 풀이
# 메모리: 35508KB / 시간: 40ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

def main():
    N, D = map(int, input().split())
    roads = {}

    for _ in range(N):
        S, E, L = map(int, input().split())

        if E > D:  # ⭐도착점이 D보다 크다면 저장 X (어차피 못가는 길)
            continue

        if S not in roads:
            roads[S] = []
        roads[S].append((E, L))
    

    def dijkstra(roads: dict) -> int:
        heap = [(0, 0)]  # 현재까지의 거리, 위치
        dist = [D+1] * (D+1)  # 가능한 최댓값은 D이므로 D+1로 거리 리스트 초기화

        while heap:
            curr_dist, curr_pos = heappop(heap)

            # 현재 위치가 D 이면 거리값 return
            if curr_pos == D:
                return curr_dist

            if dist[curr_pos] < curr_dist:
                continue

            # 1. 고속도로로 이동하는 경우
            if curr_dist + 1 < dist[curr_pos + 1]:
                dist[curr_pos + 1] = curr_dist + 1
                heappush(heap, (curr_dist + 1, curr_pos + 1))
            # 2. 지름길로 이동하는 경우
            if curr_pos in roads:
                for nxt_pos, nxt_dist in roads[curr_pos]:
                    if curr_dist + nxt_dist < dist[nxt_pos]:
                        dist[nxt_pos] = curr_dist + nxt_dist
                        heappush(heap, (curr_dist + nxt_dist, nxt_pos))
    

    print(dijkstra(roads))


main()


# 2) DP 사용 풀이
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N, D = map(int, input().split())
    roads = {}

    for _ in range(N):
        S, E, L = map(int, input().split())

        if E > D:  # ⭐도착점이 D보다 크다면 저장 X (어차피 못가는 길)
            continue

        if S not in roads:
            roads[S] = []
        roads[S].append((E, L))
    
    dp = [D+1] * (D+1)
    dp[0] = 0

    for i in range(D+1):
        if i > 0:
            dp[i] = min(dp[i], dp[i-1] + 1)
        
        if i in roads:
            for j, dist in roads[i]:
                dp[j] = min(dp[j], dp[i] + dist)  # j까지의 기존 DP값 vs i까지의 DP값 + i-j의 거리값 비교 후 갱신
    
    print(dp[D])


main()