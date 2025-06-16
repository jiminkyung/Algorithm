# 정렬  # 기하학


# 문제: https://www.acmicpc.net/problem/1485
# 참고한 글👉 https://deepdata.tistory.com/735

# 메모리: 32412KB / 시간: 56ms
from sys import stdin


input = stdin.readline

def main():
    def check_dist(p1: tuple, p2: tuple) -> int:
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    

    T = int(input())

    for _ in range(T):
        points = [tuple(map(int, input().split())) for _ in range(4)]

        # 첫 시도: p1에서 p2, p3를 변으로 가정하고(l1, l2) p1-p4는 대각선으로 가정함(l3)
        # 만약 l1 + l2 = l3를 만족하면서 l3 = p2-p3를 만족하면 정사각형으로 판별.
        # => 무작위로 p1~p4를 설정하면 X. p1-p3가 서로 대각선에 위치한 꼭짓점이 될 수도 있음.

        # 🗝️각 꼭짓점끼리의 길이를 구함. 모두 6개의 거리값이 나오게 됨.
        # 정렬 후 작은 네 길이의 값이 같다면 => 마름모
        # 두 대각선의 길이가 같다면 => 정사각형 을 만족함.
        dist = [check_dist(points[i], points[j]) for i in range(4) for j in range(i+1, 4)]
        dist.sort()

        if dist[0] == dist[1] == dist[2] == dist[3] and dist[4] == dist[5]:
            print(1)
        else:
            print(0)


main()