# 다이나믹 프로그래밍
# 재귀


# 문제: https://www.acmicpc.net/problem/2705

# DP, 재귀 문제. 나중에 다시 풀어볼만한 문제임.
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # 🚨12121은 재귀적 팰린드롬 X
    # 12 != 21 이므로... 젠장.
    dp = [0] * 1001
    dp[0] = dp[1] = 1

    def dfs(num: int) -> int:
        nonlocal dp

        if dp[num]:
            return dp[num]
        
        cnt = 1
        # dp[x]: x로 나타낼 수 있는 재귀적 팰린드롬의 갯수
        # 여기서 i는 양 쪽의 수를 나타냄. 가운뎃값은 num - 2*i인 셈.
        # 즉, 재귀를 반복하면 팰린드롬은 항상 ii 혹은 ixi의 모양을 띄게 됨.
        for i in range(1, num//2 + 1):
            cnt += dfs(i)
        dp[num] = cnt
        
        return dp[num]
    

    T = int(input())

    for _ in range(T):
        N = int(input())
        print(dfs(N))


main()