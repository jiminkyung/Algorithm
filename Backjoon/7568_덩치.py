# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/7568
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    data = [tuple(map(int, input().split())) for _ in range(N)]
    # ret[i]: i번 학생보다 덩치가 큰 학생 수 + 1 = 덩치 순위
    ret = [1] * N

    for i in range(N):
        x, y = data[i]
        for j in range(N):
            if i == j:
                continue
            p, q = data[j]
            if x < p and y < q:
                ret[i] += 1
    
    print(*ret)


main()