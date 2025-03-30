# 문자열
# 정규 표현식


# 문제: https://www.acmicpc.net/problem/1013
# 메모리: 36980KB / 시간: 108ms
from sys import stdin
import re


input = stdin.readline

def main():
    N = int(input())

    pattern = re.compile(r"(100+1+|01)+")
    for _ in range(N):
        data = input().rstrip()
        # ⭐fullmatch로 문자열 전체과 패턴이 일치하는지 확인해야함.
        if pattern.fullmatch(data):
            print("YES")
        else:
            print("NO")


main()