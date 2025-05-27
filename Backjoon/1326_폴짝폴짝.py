# 너비 우선 탐색 (BFS)


# 문제: https://www.acmicpc.net/problem/1326

"""
기존 방식
                for i in range(bridge[x], N, bridge[x]):
                    if x+i < N:
                        nxt.append((x+i, cnt+1))
                    if 0 <= x-i:
                        nxt.append((x-i, cnt+1))

굳이 저럴 필요 없이 for i in range(x % bridge[x], N, bridge[x]): 로 한번에 처리 가능.
"""
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    bridge = list(map(int, input().split()))
    a, b = map(lambda x: int(x)-1, input().split())  # 0-based 처리

    def bfs(start: int, end: int) -> int:
        """ BFS로 최단 경로 구하기 """
        visited = [False] * N
        visited[start] = True
        curr = [start]
        cnt = 0

        while curr:
            nxt = []
            cnt += 1

            for x in curr:
                # x번을 x번값으로 나눈 나머지값부터 시작.
                # => x를 기준으로 0 ~ x, x ~ N-1 범위에서 x번값만큼 떨어져있는 모든 칸 탐색
                for i in range(x % bridge[x], N, bridge[x]):
                    if not visited[i]:
                        if i == end:  # 목적지라면 cnt 반환
                            return cnt
                        visited[i] = True
                        nxt.append(i)
            curr = nxt
        return -1
    
    print(bfs(a, b))


main()