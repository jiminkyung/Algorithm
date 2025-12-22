# 브루트포스 알고리즘
# 기하학


# 문제: https://www.acmicpc.net/problem/3042
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    coord = []

    # 꼭 한칸 단위로 이어진 선분이 아니어도 됨. (예제 2번 참고)
    for i in range(N):
        line = input().rstrip()
        for j in range(N):
            if line[j] != ".":
                coord.append((i, j))
    
    L = len(coord)
    ret = 0

    # 조합 생성
    for a in range(L):
        x1, y1 = coord[a]
        for b in range(a+1, L):
            x2, y2 = coord[b]
            for c in range(b+1, L):
                x3, y3 = coord[c]

                if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
                    ret += 1
    
    print(ret)


main()