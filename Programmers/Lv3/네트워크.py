# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/43162


from collections import deque


def solution(n, computers: list[list[int]]):
    visited = [False] * n

    def bfs(start):
        nonlocal visited

        queue = deque([start])
        visited[start] = True

        while queue:
            curr = queue.popleft()

            for nxt in range(n):
                if computers[curr][nxt] and not visited[nxt]:
                    queue.append(nxt)
                    visited[nxt] = True
        
        return 1
    

    ret = 0

    for i in range(n):
        if not visited[i]:
            ret += bfs(i)
    
    return ret