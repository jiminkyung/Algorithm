# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/9466
# 반례 모음👉 https://www.acmicpc.net/board/view/143387

# 처음엔 유니온 파인드 문제인줄 알았으나, DFS를 사용하는 문제였다.
# 메모리: 48104KB / 시간: 2116ms
from sys import stdin


input = stdin.readline

def dfs(start):
    global teams

    team = [start]
    visited[start] = True
    nxt = lst[start]

    while True:
        if visited[nxt]:
            if nxt in team:  # 방문한 상태이고 team에 존재한다면,
                return len(team) - team.index(nxt)  # team 길이 - nxt의 첫번째 위치 반환
            else:
                return 0
        else:
            visited[nxt] = True
            team.append(nxt)
            nxt = lst[nxt]

for _ in range(int(input())):
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)

    teams = 0

    for i in range(1, n+1):
        if not visited[i]:
            teams += dfs(i)
    print(n - teams)


# 재귀로 푸는 방식이 유명한것같다. 코드가 더 깔끔하다.
# 출처👉 https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-9466-%ED%85%80-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

#cycle 이루는 result 반환
def dfs(v):
    global result
    visited[v] = True
    cycle.append(v)
    num = number[v]

    if visited[num]:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

#테스트 케이스만큼 실행
for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    number = [0] + list(map(int, input().split()))
    visited = [True] + [False]*N
    result = []
	
    #1~n까지 방문여부 확인하면서 dfs()호출
    for i in range(1,N+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(N-len(result))