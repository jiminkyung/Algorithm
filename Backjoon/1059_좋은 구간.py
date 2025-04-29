# 정렬


# 문제: https://www.acmicpc.net/problem/1059
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    """
    좋은 구간의 조건은 다음과 같음.
    - A < B. 여기서 A, B는 수열에 속한 수가 아니어도 됨
    - 임의의 정수 x는 A <= x < B, A < x <= B, A < x < B 중 하나를 만족해야함.
        - 다시말해 A == B인 경우만 제외하면 됨
        - 또한 이 x는 수열에 존재하지 않아야 함
    
    n은 수열에 존재하면 안됨. 존재한다면 만들 수 있는 구간 X
    수열에 존재하지 않는다면, 위 조건을 만족해야함.

    따라서 n보다 작은 수 중 최댓값 low, 큰 수 중 최솟값 high 를 구한다.
    유효한 A 범위는 low ~ n, B 범위는 n ~ high이고, A == B 일때만 제외시키면 되므로,
    => (low ~ n) * (n ~ high) - 1 이 가능한 구간 갯수가 되겠다.
    """
    L = int(input())
    S = sorted(map(int, input().split()))
    n = int(input())

    # n이 S안에 존재한다면 0 출력 후 종료
    if n in S:
        print(0)
        return
    
    low, high = 0, 1001

    for s in S:
        if s < n:
            low = s
        elif n < s:
            high = s
            break

    less = n - low  # n - (low+1) - 1
    more = high - n

    total = less * more - 1
    print(total)


main()