# 문자열
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1515
# 메모리: 32412KB / 시간: 48ms
from sys import stdin


input = stdin.readline

def main():
    target = input().strip()
    idx = 0
    n = 1

    # 숫자 n을 1씩 증가시킴.
    # n을 문자열로 변환 후, 각 자릿수를 확인함.
    # => 자릿수와 target의 idx번째 숫자와 일치하면 idx 증가.
    while idx < len(target):
        for ch in str(n):
            if idx < len(target) and target[idx] == ch:
                idx += 1
        n += 1

    print(n - 1)


main()