# 구현


# 문제: https://www.acmicpc.net/problem/2799
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    M, N = map(int, input().split())

    arr = [input().rstrip() for _ in range(5*M + 1)]
    total = [0] * 5

    # 블라인드는 위 아래로 막혀있음. 맨 위를 제외하고 5칸씩 반복된다고 생각하면 됨.
    for i in range(1, 5*M + 1, 5):
        for j in range(1, 5*N + 1, 5):  # 세로(열) 패턴도 마찬가지
            # (i, j) = 블라인드의 좌측 상단 꼭짓점(시작점)
            window = [arr[i+k][j:j+4] for k in range(4)]

            # 갯수와 번호가 일치하므로, 갯수에 해당되는 인덱스에 바로 카운팅.
            cnt = window.count("****")
            total[cnt] += 1
    
    print(*total)


main()