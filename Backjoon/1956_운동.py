# 최단 경로


# 사이클이 있어야함. 플로이드-워셜이 적절할듯싶다.
# Python3로 제출시 시간초과! => 다익스트라를 응용해서 풀어야 하나? => 플로이드-워셜이 맞았다.
# PyPy3로 제출 => 메모리: 137044KB / 시간: 1080ms
from sys import stdin


input = stdin.readline
INF = float("inf")
V, E = map(int, input().split())
roads = []

for _ in range(E):
    roads.append(tuple(map(int, input().split())))

def floyd_warshall():
    dp = [[INF] * V for _ in range(V)]

    for u, v, w in roads:
        dp[u-1][v-1] = w
    
    ret = INF

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if i == j:
                    if k != i:
                        ret = min(ret, dp[i][k] + dp[k][j])
                    else:
                        dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    
    return ret if ret != INF else -1

print(floyd_warshall())


# 다익스트라로 2차원 배열을 생성해서 풀이. => 메모리 초과...
"""
dp[start][end]로 거리값을 저장할 배열을 2차원 배열로 생성해준다.
road: 그래프를 저장할 배열
dp: 최단경로값을 저장할 배열

heap에서 꺼낸 start, end, dis(거리)값을 가지고 비교한다.
end를 시작점으로 사용하는 그래프를 순회하면서,
end -> new_end(다른 도착점의 거리값) + dis(start->end) 가 start -> new_end 의 값보다 작다면,
dp[start][new_end] = dis + end->new_end 로 업데이트.
그리고 힙에 추가해준다.

만약 최단경로가 나오지 않는다면 -1을 반환한다.
"""
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
road = [[] for _ in range(V+1)]
dp = [[INF] * (V+1) for _ in range(V+1)]
heap = []

for _ in range(E):
    a, b, c = map(int, input().split())
    road[a].append((b, c))
    dp[a][b] = c
    heappush(heap, (c, a, b))

def dijkstra():
    while heap:
        dis, start, end = heappop(heap)

        if start == end:
            return dis
        
        if dis > dp[start][end]:
            continue

        for de, dd in road[end]:
            new_dis = dd + dis
            if new_dis < dp[start][de]:
                dp[start][de] = new_dis
                heappush(heap, (new_dis, start, de))
    else:
        return -1

print(dijkstra())


# ❗ 플로이드-워셜로 Python3를 통과한 분이 있다.
import sys

def floyd_warshall(v, edges):
    dist = [[float('inf')] * v for _ in range(v)]

    for i in range(v):
        dist[i][i] = 0

    for a, b, c in edges:
        dist[a-1][b-1] = c

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    result = float('inf')
    for i in range(v):
        for j in range(v):
            if i != j and dist[i][j] != float('inf') and dist[j][i] != float('inf'):
                result = min(result, dist[i][j] + dist[j][i])

    return result if result != float('inf') else -1

input = sys.stdin.readline
v, e = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(e)]

result = floyd_warshall(v, edges)

print(result)


# 결정적인 이유를 모르겠다. 리스트를 한번에 입력받아서?
# 실제로 몇 번 굴려본 결과, min()이냐 if문이냐의 차이로 갈리는듯하다.
# 인덱싱으로 덧셈연산하는것보다 min()이 시간을 더 잡아먹는다. => 플로이드-워셜은 많은 데이터를 수행하기 때문에 작은 차이가 쌓여서 이런 현상이 나타남.
"""
시도해본것들
- 함수에 인자 직접 전달하기
    - 파이썬은 변수를 찾을때 지역범위부터 시작해 전역범위로 확장한다. 이 과정에서 추가적인 검색 시간이 소요될 수 있음.
- 리스트 컴프리헨션으로 입력값을 한번에 처리하기
- min()대신 조건문으로 최적화(약간~ 더 효율적임)
- 함수 내에서 dp 리스트 생성
    - 메모리 사용을 함수 scope로 제한, 가비지 컬렉션을 효율적으로 만든다고 함.
"""
# 메모리: 55560KB / 시간: 5120ms
from sys import stdin


input = stdin.readline
INF = float("inf")
V, E = map(int, input().split())
road = [tuple(map(int, input().split())) for _ in range(E)]

def floyd_warshall(v, road):
    dp = [[INF] * v for _ in range(v)]
    
    for i in range(v):
        dp[i][i] = 0
        
    for a, b, c in road:
        dp[a-1][b-1] = c
    
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    
    ret = INF
    for i in range(v):
        for j in range(i+1, v):
            if dp[i][j] != INF and dp[j][i] != INF:
                ret = min(ret, dp[i][j] + dp[j][i])
    
    return ret if ret != INF else -1

print(floyd_warshall(V, road))