# 그래프 이론


# 문제: https://www.acmicpc.net/problem/1115

# 단일 사이클 문제. 유형 익히기 괜찮아서 다시 풀어봐도 좋을 문제다.

# 첫 시도: permutations로 모든 순열을 구한 다음, 단일 사이클 조건을 만족하면 다른 갯수 체크. 가장 적은 갯수 갱신.
# => 시간초과!

# 굳이 순열을 만들 필요 X.
# 주어진 A(P)의 사이클 갯수를 체크한다.
# => 1개라면 이미 완벽한 수열이므로 0 출력, 2개 이상이라면 해당 갯수를 그대로 출력.

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    P = list(map(int, input().split()))
    """
    🗝️ A가 완벽한 수열이 되려면 "단일 사이클"이어야 한다.
    따라서 A의 사이클 갯수가 cnt개이고 cnt > 1 이라면, cnt개의 원소를 변경해야 완벽한 수열이 될 수 있음.
    ex) [2, 0, 1, 4, 3]의 사이클은,
    사이클 1: 0 -> 2 -> 1 -> 0
    사이클 2: 3 -> 4 -> 3
    => 사이클 1에 있는 원소와 2에 있는 원소를 스왑해야 함.
    """

    def count_cycle(A):
        visited = [False] * N
        cnt = 0

        for i in range(N):
            if not visited[i]:
                cnt += 1
                visited[i] = True
                nxt = A[i]
                while nxt != i:
                    visited[nxt] = True
                    nxt = A[nxt]
        return cnt
    

    ret = count_cycle(P)
    print(ret if ret > 1 else 0)


main()