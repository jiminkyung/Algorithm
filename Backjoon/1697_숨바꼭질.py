# 그래프와 순회

"""
수빈이의 위치 N, 동생의 위치 K
수빈이의 위치가 X일때 걷는다면 1초에 X-1 또는 X+1,
순간이동을 한다면 1초에 2*X의 위치로 이동한다.
"""

# 메모리: 32924KB / 시간: 76ms
# 스택 2개를 사용하는 방식의 풀이
N, K = map(int, input().split())
MAX = 100000
visited = [False] * (MAX + 1)

def bfs(n, k):
    visited[n] = True
    curr = [n]

    count = 0
    while curr:
        to_visit = []
        
        for c in curr:
            if c == k:
                return count
            for i in (c - 1, c + 1, c * 2):
                if 0 <= i <= MAX and not visited[i]:
                    visited[i] = True
                    to_visit.append(i)
        curr = to_visit
        count += 1

print(bfs(N, K))


# 일반적인 BFS 풀이.
# 메모리: 35220KB / 시간: 96ms
# deque 대신 list 사용, visited에 boolean 사용 등 여러가지 이유로 첫번째 코드가 더 빨랐다.
from collections import deque


N, K = map(int, input().split())
MAX = 100000
visited = [0] * (MAX + 1)

def bfs(n, k):
    queue = deque([n])

    while queue:
        node = queue.popleft()
        if node == k:
            return visited[node]      
        for i in (node - 1, node + 1, node * 2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[node] + 1
                queue.append(i)

print(bfs(N, K))