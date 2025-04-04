# BFS (너비 우선 탐색)


# 문제: https://www.acmicpc.net/problem/1327

# 일정 규칙대로 sorting 후 횟수 카운트, 해당 수열이 오름차순을 만족하면 종료.
# 메모리: 39708KB / 시간: 208ms
from sys import stdin
from collections import deque


input = stdin.readline

def main():
    N, K = map(int, input().split())
    target = tuple(i for i in range(1, N+1))  # 목표값 (오름차순 수열)
    lst = tuple(map(int, input().split()))    # 초기값

    def bfs(target: tuple, lst: tuple) -> int:
        visited = set()
        visited.add(lst)
        queue = deque([(lst, 0)])

        while queue:
            curr, cnt = queue.popleft()
            if curr == target:  # 목표값과 일치하면 바로 반환
                return cnt
            
            # i부터 K개를 뒤집는다는것은 (i, i+1 ... i+K-1)를 뒤집는것을 의미함.
            # 따라서 i+K <= N 이어야 함. 따라서 가능한 i의 범위는 (0 ~ N-K)임.
            for i in range(N-K+1):
                nxt = curr[:i] + curr[i:i+K][::-1] + curr[i+K:]
                if nxt in visited:
                    continue
                visited.add(nxt)
                queue.append((nxt, cnt+1))
        return -1
    
    print(bfs(target, lst))


main()