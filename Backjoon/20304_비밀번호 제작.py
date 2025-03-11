# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/20304

# 비트마스킹 + BFS 문제.
# ⭐ 주어진 수 N의 길이만큼만 탐색하면 훨씬 효율적임!

# 메모리: 69308KB / 시간: 2808ms
from sys import stdin
from collections import deque


input = stdin.readline

def main():
    def bfs() -> int:
        visited = [-1] * (N+1)  # visited[x]: 비밀번호를 x로 설정했을때의 안전거리
        queue = deque(pwd)
        length = len(bin(N)) - 2  # 0b1101 이런식으로 나오므로 0b 자릿수를 빼줘야 함

        # 이미 시도한 비밀번호들의 안전거리를 0으로 설정
        for q in queue:
            visited[q] = 0
        
        while queue:
            curr = queue.popleft()

            for i in range(length):  # 🗝️N의 이진수 길이만큼만 체크
                nxt = curr ^ (1 << i)
                if nxt <= N and visited[nxt] == -1:
                    visited[nxt] = visited[curr] + 1  # 자릿수 하나만 바꿨으므로 안전거리는 1
                    queue.append(nxt)
        return max(visited)


    N = int(input())
    _ = int(input())
    pwd = list(map(int, input().split()))
    
    print(bfs())


main()


# 20비트(10^6)까지 탐색하는 풀이.
# 메모리: 113376KB / 시간: 3116ms
from sys import stdin
from collections import deque

input = stdin.readline


def main():
    def bfs() -> int:
        visited = [False] * (N+1)  # 해커가 시도한 비밀번호는 방문 처리
        queue = deque()
        for p in pwd:
            queue.append((p, 0))  # (비밀번호, 현재 안전 거리)
            visited[p] = True

        max_safety = 0

        while queue:
            curr, dist = queue.popleft()
            max_safety = max(max_safety, dist)

            # 비트 한 자리씩 바꿔서 새로운 숫자 생성
            for i in range(20):  # 20비트(최대 10^6)까지만 탐색
                nxt = curr ^ (1 << i)  # i번째 비트를 toggle

                if 0 <= nxt <= N and not visited[nxt]:
                    visited[nxt] = True
                    queue.append((nxt, dist + 1))

        return max_safety
    
    N = int(input())
    _ = int(input())
    pwd = list(map(int, input().split()))
    
    print(bfs())


main()