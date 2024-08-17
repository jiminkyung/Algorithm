# 최단 경로

# BFS, 다익스트라 알고리즘 중 선택 사용 가능


# 다익스트라 알고리즘 사용 풀이
# 메모리: 37044KB / 시간: 124ms
from sys import stdin
import heapq


input = stdin.readline
N, K = map(int, input().split())
MAX = 100000

def dijkstra(start, end) -> int:
    time = [float("inf")] * (MAX+1)  # 100001개의 inf로 이루어진 리스트 time 생성
    time[start] = 0
    queue = [(0, start)]

    while queue:
        curr_time, curr_node = heapq.heappop(queue)

        if curr_node == end:  # 만약 현재 노드가 end(K)라면 time[현재노드]값을 반환한다.
            return time[curr_node]
        
        # X-1, X+1은 1초, X*2는 0초가 소요된다.
        # 조건에 맞춰 (소요되는 시간, 이동할 좌표) 튜플을 순회한다.
        for t, n in ((1, curr_node+1), (1, curr_node-1), (0, curr_node*2)):
            if 0 <= n <= MAX:  # 만약 이동할 좌표가 좌표계 범위내에 존재한다면,
                new_time = curr_time + t  # 현재까지의 시간값 + 이동할 좌표의 소요시간을 더한다.

                if new_time < time[n]:  # 위에서 구한 시간값이 현재 기록되어있는 시간값보다 작다면,
                    time[n] = new_time  # 새로 구한 시간값으로 변경하고 힙에 추가한다.
                    heapq.heappush(queue, (new_time, n))

print(dijkstra(N, K))


# BFS를 사용한 풀이. 이게 더 빨랐다! => 간단한 조건(0 or 1), 단순한 큐 기능
# 메모리: 34296KB / 시간: 76ms
from collections import deque


def bfs(start, end):
    queue = deque([(start, 0)])  # (위치, 시간)
    visited = [False] * 100001  # visited를 리스트로 변경
    visited[start] = True
    
    while queue:
        position, time = queue.popleft()
        
        if position == end:
            return time
        
        # 2X 이동 (0초 소요)
        if position * 2 <= 100000 and not visited[position * 2]:
            visited[position * 2] = True
            queue.appendleft((position * 2, time))  # 우선 처리를 위해 왼쪽에 추가
        
        # X-1, X+1 이동 (1초 소요)
        for next_pos in (position - 1, position + 1):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))
        
        # 🚨 한 번 확인한곳은 넘어가는 이유?
        # 1. 이동시간이 0과 1뿐임.
        # 2. 0초로 갈수있는곳(X*2)을 무조건 1보다 먼저 확인함.

N, K = map(int, input().split())
print(bfs(N, K))