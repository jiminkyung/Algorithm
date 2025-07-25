# 구현
# 그리디 알고리즘
# 많은 조건 분기


# 문제: https://www.acmicpc.net/problem/1783
# 메모리: 32412KB / 시간: 36ms
"""
규칙으로 푸는 문제다.
병든 나이트는 어느 방향으로 가든 오른쪽으로 이동함.

이해하기 쉬운 글👉 https://velog.io/@guswlsdl0121/%EB%B0%B1%EC%A4%80-1783%EB%B2%88-%EB%B3%91%EB%93%A0-%EB%82%98%EC%9D%B4%ED%8A%B8-with-Java-25bw2hsa
"""
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())

    def check(N, M):
        # 세로가 1이라면 처음 위치 한칸만 가능
        if N == 1:
            return 1
        # 세로가 2라면 가로 길이에 따라 결정됨.
        # 5칸 이상 방문할경우 모든 방향을 사용해야하지만, 세로 길이가 2인 이상 오른쪽-왼쪽 이동만 가능함.
        # 따라서 최대값은 min(4, 가능한 칸 수)
        elif N == 2:
            return min(4, (M + 1) // 2)
        # 세로 >=3 일경우 (위-아래 이동 가능)
        else:
            # 모든 방향을 사용하려면 (초기위치 1칸 + 4방향 이동 6칸) = 7칸이 필요함.
            # 따라서 가로가 7 미만이면 min(4, M)이 최대값이 됨.
            if M < 7:
                return min(4, M)
            # 세로 >= 3, 가로 >= 7이라면 4방향 모두 사용 가능함.
            # 항상 오른쪽으로 이동하므로 위-아래로만 이동하는게 효율적임.
            # 따라서 4방향 조건 충족 후 위-아래로만 움직이면 됨.
            # => 왼쪽-오른쪽 방향 이동 시 오른쪽으로 1칸씩 더 감. 따라서 최대값은 M-2.
            else:
                return M - 2

    print(check(N, M))


main()