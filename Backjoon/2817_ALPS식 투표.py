# 구현
# 정렬


# 문제: https://www.acmicpc.net/problem/2817
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    X = int(input())
    N = int(input())

    # 이름이 A-Z 인 스태프의 점수
    score = [-1] * 26

    # 점수집합들
    union = []
    base = X * 0.05  # 기준점

    for _ in range(N):
        name, num = input().rstrip().split()
        num = float(num)
        name = ord(name) - 65  # 알파벳으로 주어진 이름을 정수형으로 변환 A-Z = 0-25

        # 기준치 미만이면 넘어감
        if num < base:
            continue

        # 기준(5% 이상)을 만족했으나 최종 칩 갯수가 0인 스태프들도 출력해야함.
        # 일단 기준치 이상인 스태프들의 점수를 0으로 갱신.
        score[name] = 0

        for i in range(1, 15):
            val = num / i
            union.append((val, name))
    
    union.sort(reverse=True)

    for _, name in union[:14]:
        score[name] += 1

    for i, s in enumerate(score):
        # 기준치를 넘었던 스태프들만 점수 출력
        if s >= 0:
            print(chr(i + 65), s)


main()