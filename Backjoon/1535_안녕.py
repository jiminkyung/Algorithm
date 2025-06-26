# 다이나믹 프로그래밍  # 냅색 문제
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1535
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    strength = list(map(int, input().split()))
    pleasure = list(map(int, input().split()))

    # dp[a][b]: a번째 사람까지 선택, 체력이 b일때의 최대 기쁨 수치
        # 🚨-1로 초기화하는게 나음. 0으로 초기화 시 가능한 경우가 아님에도 처리해버림.
        # ex) 첫번째 사람의 체력, 기쁨이 (60, 10)이고 두번째 사람의 체력, 기쁨이 (20, 15)일경우,
        # dp[0][30] = 0 (체력 30 남음, 기쁨 0)은 가능한 상태가 아님. 하지만 두번째 사람 처리 시 가능하다고 판단해버림.
        # => dp[1][10] = 15 라는 잘못된 값이 저장되어버림.
        # => 어차피 정답은 제대로 처리된 값이 선택되겠지만, 쓸데없는 쓰레기값들이 저장된다.
    dp = [[-1] * 101 for _ in range(N)]
    # 첫번째 사람의 경우 미리 처리
    dp[0][100] = 0
    if 100 - strength[0] > 0:
        dp[0][100 - strength[0]] = pleasure[0]

    for i in range(1, N):
        s, p = strength[i], pleasure[i]
        for j in range(101):
            if dp[i - 1][j] != -1:
                # i번째 사람 선택 X
                # (i, j) 조합은 이 때 처음 등장하는것이므로, max 없이 바로 이전값을 가져와도 된다.
                dp[i][j] = dp[i - 1][j]

                # i번째 사람 선택 O
                # 이 경우, j-s는 이전의 j였을 가능성이 있으므로 max로 비교해줘야함.
                if j - s > 0:
                    dp[i][j - s] = max(dp[i][j - s], dp[i - 1][j] + p)

    print(max(dp[N - 1]))


main()