# 정렬
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2548
# 메모리: 34456KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    # 🗝️정렬 후 중간에 위치한 값이 제일 합 차이가 적음.
    # 홀수개면 정중앙, 짝수개면 중앙 두개를 비교해서 결정해야함.
    nums = sorted(map(int, input().split()))
    ret = -1

    if N % 2 == 0:
        diff_1 = sum(abs(nums[N//2 - 1] - num) for num in nums)
        diff_2 = sum(abs(nums[N//2] - num) for num in nums)

        ret = nums[N//2 - 1] if diff_1 <= diff_2 else nums[N//2]
    else:
        ret = nums[N//2]

    print(ret)


main()