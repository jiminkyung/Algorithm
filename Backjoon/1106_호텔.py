# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/1106

# 냅색 문제.
# 메모리: 32544KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    C, N = map(int, input().split())
    cities = [tuple(map(int, input().split())) for _ in range(N)]
    
    # 최소 C명을 확보해야하는 상황임.
    # 기본값으로 한 도시에서 얻을 수 있는 고객의 수는 최대 100명.
    # => 즉, 정확히 C명만 얻을 수 없는 상황일때를 고려하는거임.
    # => C + x 만큼의 고객을 얻어야 할 때, 나올 수 있는 최댓값은 C + 100명.
    # 따라서 맥시멈을 C + 100으로 설정하고 DP 진행. 그 이상은 무의미함.
    max_people = C + 100

    # dp[x]: x명을 얻기 위한 최소 비용
    dp = [float("inf")] * (max_people + 1)
    dp[0] = 0

    # 가격-고객수 리스트를 순회하며 고객수 ~ 최대고객수(C+100)까지 얻을 경우를 체크
    for cost, people in cities:
        for i in range(people, max_people+1):
            # 배수의 경우는 DP를 진행하며 자연스럽게 계산됨.
            # ex) 3원으로 5명을 얻을 수 있을때, dp[5] = 3이라고 가정
            # dp[10] = min(dp[10], dp[5] + 3)
            # dp[15] = min(dp[15], dp[10] + 3) ... 이런식으로
            dp[i] = min(dp[i], dp[i - people] + cost)
    
    # 최소 C명을 구하기위한 최소비용
    ret = min(dp[C:])
    print(ret)


main()