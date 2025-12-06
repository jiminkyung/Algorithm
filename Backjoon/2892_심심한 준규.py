# 애드 훅
# 비트마스킹


# 문제: https://www.acmicpc.net/problem/2892
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # 공백(32)과 0~9 XOR범위(십진수): 16 ~ 25
    # 온점(.)과 0~9 XOR범위(십진수): 22 ~ 31
    # -> 십진수로 변환했을때의 값이 16 ~ 31 이면 문자열 X

    N = int(input())
    nums = list(input().rstrip().split())

    ret = ["-"] * len(nums)
    for i, num in enumerate(nums):
        if 16 <= int(num, 16) <= 31:
            ret[i] = "."
    
    print(*ret, sep="")


main()