# 구현
# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/2491

# 🚨LIS, LDS(가장 긴 증가하는/감소하는 부분수열) 문제인줄 알았으나 아니었음.
# 문제에서 말하는 "연속되는"은 인덱스를 말한 것. 붙어있는 수열 중 가장 긴 수열을 골라야 함.

# 메모리: 40900KB / 시간: 72ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    nums = list(map(int, input().split()))

    def calc(lst: list) -> tuple[int, int]:
        dp = [1] * N    # 증가하는 수열
        dp_r = [1] * N  # 감소하는 수열

        for i in range(N-2, -1, -1):
            if lst[i] <= lst[i+1]:
                dp[i] = dp[i+1] + 1
            
            if lst[i] >= lst[i+1]:
                dp_r[i] = dp_r[i+1] + 1

        lis, lds = max(dp), max(dp_r)
        return max(lis, lds)
    

    ret = calc(nums)
    print(ret)


main()