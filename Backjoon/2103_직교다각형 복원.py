# 정렬
# 기하학


# 문제: https://www.acmicpc.net/problem/2103
# 나중에 다시 풀어볼만한 문제

# 메모리: 42088KB / 시간: 196ms
from sys import stdin
from collections import defaultdict


input = stdin.readline

def main():
    """
    처음엔 외곽선을 따라가는 방식으로 풀었지만 실패.
    🗝️좌표를 압축하는 방식으로 풀어야 깔끔하다.

    - 같은 x좌표/y좌표를 가진 점들끼리 그룹화한다.
    - 각 그룹을 정렬 후 인접한 쌍 끼리의 거리를 합산한다.

    ⭐같은 축 좌표를 가진 점들은 항상 "짝수"개임.
    따라서 정렬했을때 인접한 쌍들이 실제 외곽선을 나타내는 셈이다.
    ex) y = 3일때 x좌표들 = [1, 3, 4, 5, 8]
    - [1, 3], [4, 5] 끼리 매칭
    - y = 3일때의 실제 외곽선 길이는 (3-1) + (5-4) = 2 + 1 = 3이 된다!

    참고 설명글👉 https://maramarathon.tistory.com/6
    """
    N = int(input())
    coord = [tuple(map(int, input().split())) for _ in range(N)]
    coord.sort()

    X = defaultdict(list)
    Y = defaultdict(list)

    for x, y in coord:
        X[x].append(y)
        Y[y].append(x)
    
    length = 0

    # y축 평행선들
    for lst in X.values():
        length += sum(lst[i+1] - lst[i] for i in range(0, len(lst)-1, 2))
    
    # x축 평행선들
    for lst in Y.values():
        length += sum(lst[i+1] - lst[i] for i in range(0, len(lst)-1, 2))
    
    print(length)


main()