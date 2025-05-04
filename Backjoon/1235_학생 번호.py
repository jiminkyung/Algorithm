# 문자열


# 문제: https://www.acmicpc.net/problem/1235
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    numbers = [input().rstrip() for _ in range(N)]
    length = len(numbers[0])

    # 뒤에서부터 1 ~ length(번호 전체 길이)만큼을 체크
    # 만약 모두 고유하다면 해당 길이 출력
    for size in range(1, length+1):
        diff = set()
        for num in numbers:
            diff.add(num[length-size:])
        
        if len(diff) == len(numbers):
            print(size)
            break


main()