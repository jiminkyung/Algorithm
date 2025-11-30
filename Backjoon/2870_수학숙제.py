# 문자열
# 정렬
# 파싱


# 문제: https://www.acmicpc.net/problem/2870
# 메모리: 37004KB / 시간: 108ms
from sys import stdin
import re


input = stdin.readline

def main():
    N = int(input())
    ret = []

    for _ in range(N):
        data = input().rstrip()
        # 숫자로 이루어진 부분만 뽑아내서 ret에 저장.
        # 숫자의 앞에 0이 나오는 경우에는 생략 가능하므로 정수형으로 변환.
        nums = list(map(int, re.findall(r"\d+", data)))
        ret.extend(nums)
    
    ret.sort()

    print(*ret, sep="\n")


main()