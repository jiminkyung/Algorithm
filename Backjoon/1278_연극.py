# 수학
# 비트마스킹
# 재귀


# 문제: https://www.acmicpc.net/problem/1278

# 비트마스킹 + DFS로 풀면 시간초과 or 메모리초과다...
# 계속 위 방식만 고집하다가, 정답 풀이를 참고함.
# => 다른 언어는 몰라도 Python으로 이 문제를 풀려면, 하노이의 탑 로직을 참고해서 풀어야 함.

# 다시 풀어볼만한 문제.
# 최적화하면 비트마스킹으로 풀 수 있지 않을까..? 나중에 다시 시도해보자~

# 메모리: 36608ms / 시간: 80ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    ret = []

    for i in range(1, N+1):
        length = len(ret)
        ret.append(i)
        # ⭐ 기존 이동을 역순으로 복제해야함
        for j in range(length-1, -1, -1):
            ret.append(ret[j])
    
    ret.append(N)

    print(len(ret)-1)  # 마지막 이동은 장면에 포함되지 않는 이동이므로 -1 처리
    print(*ret, sep="\n")


main()


# 계속 실패했던 코드... 비트마스킹 + DFS(백트래킹) 사용
import sys


sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    N = int(input())
    
    visited = [False] * (1 << N)
    curr = []
    ret = []

    def dfs(depth, state):
        nonlocal ret

        # 무대가 비었고, 시작 전이 아니라면
        if state == 0 and depth != 0:
            if depth > len(ret):  # 기존 장면 수 보다 크다면 갱신
                ret = curr[:]
            return
        
        for i in range(N):
            bit = 1 << i
            
            # 1. i번째 배우가 이미 무대에 있다면 퇴장시킴
            if state & bit:
                nxt = state & ~bit
            # 2. 무대에 없다면 입장시킴
            else:
                nxt = state | bit
            
            # 이미 사용한 조합이라면 패스
            if visited[nxt]:
                continue
            if bin(state ^ nxt).count("1") != 1:
                continue

            visited[nxt] = True
            curr.append(i)
            dfs(depth+1, nxt)
            curr.pop()
            visited[nxt] = False
    

    dfs(0, 0)

    print(len(ret) - 1)
    for i in range(len(ret)):
        print(ret[i] + 1)


main()