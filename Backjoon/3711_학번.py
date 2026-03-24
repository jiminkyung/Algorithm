# 수학
# 브루트포스 알고리즘
# 정수론
# 집합과 맵


# 문제: https://www.acmicpc.net/problem/3711
# 메모리: 32412KB / 시간: 696ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    for _ in range(N):
        solve()


def solve():
    G = int(input())
    numbers = [int(input()) for _ in range(G)]

    # 서로 다른 나머지가 최소 G개 나와야 함 (0 ~ G-1), 따라서 m의 시작값을 G로 설정.
    # 또한 각각의 num 값 자체가 나머지가 될 때만 len(remains) == G 를 만족할수도 있음,
    # 최대 m값은 num 중 가장 큰 값보다 + 1 인 값으로 설정.
    for i in range(G, max(numbers) + 2):
        remains = {num % i for num in numbers}
        
        if len(remains) == G:
            print(i)
            break


main()