# 구현
# 정렬


# 문제: https://www.acmicpc.net/problem/2628
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    M, N = map(int, input().split())
    R = [0, N]  # 가로로 자르는 구간
    C = [0, M]  # 세로로 자르는 구간

    K = int(input())
    for _ in range(K):
        num, x = map(int, input().split())

        if num == 0:
            R.append(x)
        else:
            C.append(x)
    
    R.sort()
    C.sort()

    # 구간의 길이 계산
    # ex) 만약 R = [0, 2, N]고 C = [0, 4, M]이면 구간별 크기는 [2, N-2], [4, M-4]가 됨.
    # 각 (R, C)조합을 구하고, 곱하면 구간의 넓이를 구할 수 있음.
    R = [R[i+1] - R[i] for i in range(len(R)-1)]
    C = [C[i+1] - C[i] for i in range(len(C)-1)]

    max_size = 0

    for r in R:
        for c in C:
            if max_size < r * c:
                max_size = r * c
    
    print(max_size)


main()