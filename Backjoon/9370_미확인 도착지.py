# 최단 경로

# 🚨 distance 초기화할때 float("inf")를 사용하면 틀렸다고 처리됨.
# 부동소수점 오류인것같다... int(1e9)로 고쳐넣었더니 통과.
# 이것때문에 30분은 까먹은듯. 앞으로는 최대/최소값 비교하는게 아니면 int(1e9)를 사용하자.


# 메모리: 45768KB / 시간: 292ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline
T = int(input())

def dijkstra(start):
    distance = [int(1e9)] * (n+1)
    distance[start] = 0
    queue = [(0, start)]

    while queue:
        curr_dis, curr_node = heappop(queue)

        if curr_dis > distance[curr_node]:
            continue

        for v, d in road[curr_node]:
            new_dis = curr_dis + d
            if new_dis < distance[v]:
                distance[v] = new_dis
                heappush(queue, (new_dis, v))
    return distance

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    road = [[] for _ in range(n+1)]  # 그래프를 담을 리스트
    g_to_h = 0  # g-h 간의 거리
    ret = []

    for _ in range(m):
        a, b, d = map(int, input().split())
        if (a, b) == (g, h) or (a, b) == (h, g):  # g-h, h-g인경우 거리값 d를 저장한다.
            g_to_h = d
        road[a].append((b, d))
        road[b].append((a, d))
    
    from_s = dijkstra(s)  # s부터 n까지
    from_g = dijkstra(g)  # g부터 n까지
    from_h = dijkstra(h)  # h부터 n까지

    for _ in range(t):
        target = int(input())

        path1 = from_s[g] + g_to_h + from_h[target]  # 첫번째 경우: s - g - h - 목적지
        path2 = from_s[h] + g_to_h + from_g[target]  # 두번째 경우: s - h - g - 목적지
        path = min(path1, path2)  # 둘 중 더 작은 값을 저장함

        if path <= from_s[target]:  # 만약 계산한 값이 s - 목적지 까지의 최단거리값보다 작거나 같다면,(사실상 작을경우는 없음)
            ret.append(target)  # 가능한 목적지라는 소리이므로 결과에 추가.
    
    ret.sort()
    print(" ".join(map(str, ret)))