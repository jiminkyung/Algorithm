# 정렬


# 문제: https://www.acmicpc.net/problem/1015
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    # A의 각 원소를 오름차순으로 정렬했을때, 몇번째 인덱스에 위치하는지 기록.
    # ex) 2 3 1을 오름차순 정렬하면 1 2 3이 됨. 인덱스로는 0 1 2가 되고,
    # A의 해당 숫자 위치에 이 인덱스를 넣어주면 B는 오름차순 배열이 된다.
    # 1-0, 2-1, 3-2이고 원 배열(A)는 2 3 1이니, P가 1 2 0이 되어야 함.

    N = int(input())
    A = list(map(int, input().split()))
    P = [0] * N

    arr = sorted((A[i], i) for i in range(N))

    for i, (_, idx) in enumerate(arr):
        P[idx] = i

    print(*P)


main()