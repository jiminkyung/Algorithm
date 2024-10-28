# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/9576
# 참고👉 https://dev-scratch.tistory.com/72

# 그리디, 이분매칭 알고리즘을 통해 풀 수 있는 문제다.

# 1. 그리디
"""
b가 작을수록 범위가 좁을 확률이 높아지므로 먼저 b를 기준으로 정렬한다.
b가 같다면, a가 작을수록 겹칠 확률이 낮아진다.
=> 따라서 정렬 순위는 b, a가 된다.

(2, 4), (1, 4), (4, 4) 일 경우 정렬 후 (1, 4), (2, 4), (4, 4) 순으로 배치됨.
a~b까지 탐색하면서 가장 적은 번호의 책을 부여하므로 겹치는 경우 없이 가져갈 수 있다.
"""
# 메모리: 31120KB / 시간: 84ms
from sys import stdin


input = stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())

    books = [False] * (N+1)
    req = []

    for _ in range(M):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        req.append((a, b))

    req.sort(key=lambda x: (x[1], x[0]))  # b를 기준으로 오름차순 정렬, 같다면 a를 기준으로 오름차순.

    for a, b in req:
        for i in range(a, b+1):
            if not books[i]:
                books[i] = True
                break
    
    print(sum(books))


# 2. 이분 매칭
"""
books에 책의 소유권자들을 저장할 예정.
책의 범위들을 이중리스트로 저장한다. req = [[책범위 1], [책범위 2]]
M명의 학생을 순회하며, 각 학생마다 visited를 생성 후 dfs를 실행한다.

dfs 실행 시 가능한 책 범위를 순회한다.
만약 해당 책을 방문한 상태라면 continue, 아니라면 방문체크를 해준다.
이 책을 아무도 가지고 있지 않거나, 현재 가지고 있는 주인이 다른 책을 가질 수 있다면(dfs(books[책])),
해당 책의 소유권자를 현재 학생으로 업데이트한다.

dfs(books[책]) -> 해당 책의 주인이 다른 책을 가질 수 있는지 체크
=> visited 체크 시 원래의 책은 이미 방문처리 되었으므로, continue를 통해 다음 책으로 넘어간다.
=> 그 다음은 위의 과정을 반복한다.
"""
# 메모리: 61964KB / 시간: 5868ms
import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    for node in req[x]:
        if visited[node]:
            continue
        visited[node] = True

        if books[node] == 0 or dfs(books[node]):
            books[node] = x
            return True
    return False

for _ in range(int(input())):
    N, M = map(int, input().split())
    books = [0] * (N+1)
    req = [0]
    cnt = 0

    for _ in range(M):
        a, b = map(int, input().split())
        req.append(list(range(a, b+1)))
    
    for i in range(1, M+1):
        visited = [False] * (N+1)
        if dfs(i):
            cnt += 1
    print(cnt)