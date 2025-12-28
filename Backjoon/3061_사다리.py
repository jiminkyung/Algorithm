# 그리디 알고리즘
# 정렬


# 문제: https://www.acmicpc.net/problem/3061
# 메모리: 32412KB / 시간: 1152ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        N = int(input())
        nums = list(map(int, input().split()))

        cnt = 0

        # i번째 숫자 < j번째 숫자여야 함.
        # 역순 쌍 갯수 = 필요한 가로줄 수
        for i in range(N):
            for j in range(i+1, N):
                # 앞(왼쪽)에 위치했는데 더 큰 경우 -> swap 필요
                if nums[i] > nums[j]:
                    cnt += 1
        
        print(cnt)


main()