# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/1963

# BFS도 사용하는 문제다.
# 9999까지 소수판별을 진행 후, BFS를 통해 비밀번호의 각 자리를 다른 숫자로 바꿔나간다.
# 만약 바꾼 비밀번호가 새로운 비밀번호와 일치하다면 카운트를 반환, 끝까지 일치하지 않는다면 Impossible을 반환한다.

# 1. 리스트를 이용한 BFS
# 메모리: 32412KB / 시간: 88ms
from sys import stdin


input = stdin.readline

def bfs(pwd, target):
    curr = [(pwd, 0)]
    visited = [False] * 10000
    visited[pwd] = True

    while curr:
        nxt = []

        for curr_pwd, cnt in curr:
            if curr_pwd == target:
                return cnt

            for i in range(4):
                based = list(str(curr_pwd))
                for digit in range(10):
                    if (i, digit) == (0, 0):  # 네 자리 중 첫번째 자리에는 0이 올 수 없으므로 패스
                        continue
                    based[i] = str(digit)
                    new_pwd = int("".join(based))

                    if not visited[new_pwd] and primes[new_pwd]:
                        visited[new_pwd] = True
                        nxt.append((new_pwd, cnt+1))
        curr = nxt
    return "Impossible"


primes = [True] * 10000
primes[0] = primes[1] = False

for i in range(2, 101):
    if primes[i]:
        for j in range(i*i, 10000, i):
            primes[j] = False

for _ in range(int(input())):
    curr, nxt = map(int, input().split())
    print(bfs(curr, nxt))


# 2. deque를 이용한 일반적인 BFS
# 웬만하면 deque 모듈보단 일반 리스트를 사용하는게 더 효율이 좋아서... 하지만 가독성은 역시 deque를 사용하는게 낫다.
# 메모리: 34968KB / 시간: 108ms
from sys import stdin
from collections import deque


input = stdin.readline

def bfs(pwd, target):
    queue = deque([(pwd, 0)])
    visited = [False] * 10000
    visited[pwd] = True

    while queue:
        curr_pwd, cnt = queue.popleft()

        if curr_pwd == target:
            return cnt
        
        for i in range(4):
            based = list(str(curr_pwd))
            for digit in range(10):
                if (i, digit) == (0, 0):
                    continue
                based[i] = str(digit)
                new_pwd = int("".join(based))

                if not visited[new_pwd] and primes[new_pwd]:
                    visited[new_pwd] = True
                    queue.append((new_pwd, cnt+1))
    return "Impossible"


primes = [True] * 10000
primes[0] = primes[1] = False

for i in range(2, 101):
    if primes[i]:
        for j in range(i*i, 10000, i):
            primes[j] = False

for _ in range(int(input())):
    curr, nxt = map(int, input().split())
    print(bfs(curr, nxt))