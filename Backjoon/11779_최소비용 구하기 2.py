# 동적 계획법과 최단거리 역추적


# 가중치가 있는 간선, 음의 가중치 없음, 시작점 정해져있음 => 다익스트라!
# 문제를 끝까지 읽자... 답을 요하는 시작점/도착점이 따로 없는줄알고 플로이드워셜로 작성했었다...

# 메모리: 57396KB / 시간: 276ms

from sys import stdin
import heapq


input = stdin.readline
INF = int(1e9)

def dijkstra(route: list, v, start, end):
    heap = [(start, 0)]
    costs = [INF] * (v+1)
    costs[start] = 0
    path = [0] * (v+1)

    while heap:
        curr, dis = heapq.heappop(heap)

        if dis > costs[curr]:
            continue
        
        for dn, dd in route[curr]:
            new_dis = dis + dd
            if costs[dn] > new_dis:  # dn까지의 값이 현재까지의 값 > 새로운 값 이라면 변경해준다.
                costs[dn] = new_dis
                heapq.heappush(heap, (dn, new_dis))
                path[dn] = curr  # curr -> dn 이므로 역추적을 위해 path에도 저장.
    
    return costs[end], path

n = int(input())
m = int(input())
route = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    route[u].append((v, w))

s, e = map(int, input().split())

cost, path = dijkstra(route, n, s, e)

tmp = e
ret = []
while tmp != 0:
    ret.append(tmp)
    tmp = path[tmp]

print(cost)
print(len(ret))
print(*ret[::-1])